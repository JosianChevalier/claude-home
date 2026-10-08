"""Sources de la donnée /usage — port + adaptateurs (SPI, hexagonal). PORTABLE.

Port : `get() -> Snapshot | None` (données au format /usage + horodatage). Le cœur
(quota_core) ne sait pas d'où vient la donnée ; le plugin compose les sources.

Adaptateurs :
  StatusLine  lit l'instantané que ~/.claude/statusline.py dépose à CHAQUE requête
              Claude Code (rate_limits). Gratuit, toujours à jour tant qu'on travaille.
  Http        endpoint OAuth non documenté (= /usage) + cache disque. Coûteux, rate-limité.
  Fallback    la source la plus fraîche gagne ; on ne tape le réseau que si tout est
              périmé (STALE_AFTER), si le reset de session est atteint, ou sur --force.
"""
import json
import os
import time
import urllib.request
from collections import namedtuple
from datetime import datetime, timezone

import quota_core as core

USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
CRED_FILE = os.path.expanduser("~/.claude/.credentials.json")
CACHE_FILE = os.path.expanduser("~/.claude/quota/.usage-cache.json")
STATUSLINE_FILE = os.path.expanduser("~/.claude/quota/.statusline-snapshot.json")

# Au-delà de cet âge, un instantané ne vaut plus rien : on rappelle l'API.
# Sert aussi de throttle anti-429 : après un fetch OK, pas d'appel avant STALE_AFTER.
STALE_AFTER = 600  # secondes

Snapshot = namedtuple("Snapshot", "data fetched_at")


def age(snap, now=None):
    return max(0, int((now or time.time()) - snap.fetched_at))


def freshest(*snaps):
    snaps = [s for s in snaps if s]
    return max(snaps, key=lambda s: s.fetched_at) if snaps else None


def _read_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def _write_json(path, obj):
    """Écriture atomique : un lecteur concurrent ne voit jamais un fichier tronqué."""
    tmp = f"{path}.tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f)
    os.replace(tmp, path)


# ------------------------------------------------------------------ status line
def normalize_rate_limits(rl):
    """rate_limits (status line) -> format /usage : used_percentage -> utilization,
    resets_at epoch -> ISO. Fenêtre absente (Claude Code la retire au reset) = absente."""
    out = {}
    for k in ("five_hour", "seven_day"):
        w = (rl or {}).get(k)
        if w and w.get("resets_at") is not None:
            iso = datetime.fromtimestamp(w["resets_at"], timezone.utc).isoformat()
            out[k] = {"utilization": w.get("used_percentage") or 0, "resets_at": iso}
    return out


def publish_rate_limits(rl, path=STATUSLINE_FILE, now=None):
    """Côté status line : dépose rate_limits brut + horodatage. Zéro dépendance."""
    _write_json(path, {"at": now or time.time(), "rate_limits": rl})


class StatusLine:
    def __init__(self, path=STATUSLINE_FILE):
        self.path = path

    def get(self):
        raw = _read_json(self.path)
        if not raw or "rate_limits" not in raw:
            return None
        return Snapshot(normalize_rate_limits(raw["rate_limits"]), raw["at"])


# ------------------------------------------------------------------------ http
def token_from_file():
    """Token OAuth depuis le fichier credentials (portable). None si absent.
    Le repli OS (Keychain, Credential Manager) est du ressort du host."""
    try:
        return _read_json(CRED_FILE)["claudeAiOauth"]["accessToken"]
    except Exception:
        return None


class Http:
    """get() = cache disque, sans réseau. refresh() = appel API + mise en cache."""

    def __init__(self, get_token=token_from_file, path=CACHE_FILE, fetch=None):
        self.get_token = get_token
        self.path = path
        self._fetch = fetch or self._fetch_http

    def get(self):
        c = _read_json(self.path)
        return Snapshot(c["data"], c["fetched_at"]) if c else None

    def refresh(self):
        token = self.get_token()
        if not token:
            raise RuntimeError("Token introuvable (fichier credentials ou Keychain)")
        data = self._fetch(token)
        snap = Snapshot(data, time.time())
        try:
            _write_json(self.path, snap._asdict())
        except Exception:
            pass
        return snap

    @staticmethod
    def _fetch_http(token):
        req = urllib.request.Request(USAGE_URL, headers={
            "Authorization": f"Bearer {token}",
            "anthropic-beta": "oauth-2025-04-20",
        })
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.load(r)


# -------------------------------------------------------------------- fallback
class Fallback:
    """(snapshot, erreur). erreur != None = snapshot servi en repli après un échec
    réseau (ou None si aucun repli). Sinon la donnée est jugée à jour."""

    def __init__(self, *sources, http, stale_after=STALE_AFTER):
        self.sources = sources
        self.http = http
        self.stale_after = stale_after

    def get(self, force=False, now=None):
        best = freshest(*(s.get() for s in self.sources), self.http.get())
        if best and not force and not self.is_stale(best, now):
            return best, None
        try:
            return self.http.refresh(), None
        except Exception as e:
            return best, f"Erreur API : {e}"

    def is_stale(self, snap, now=None):
        if age(snap, now) >= self.stale_after:
            return True
        # Reset de session atteint : la fenêtre est révolue quel que soit l'âge.
        return core.echeance_passee(snap.data, now and datetime.fromtimestamp(now, timezone.utc))
