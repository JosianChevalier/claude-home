"""Cœur PORTABLE du plugin quota Claude Code — calculs, réseau, cache, token-fichier.

ZÉRO appel spécifique à un OS : tout ce qui touche le système (Keychain, LaunchAgent,
osascript) ou un format d'hôte (syntaxe SwiftBar) vit dans un host_*.py à côté.
N'importe quel host (SwiftBar macOS, tray Windows) importe ce module pour la logique.
Couvert par test_quota.py.
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
CRED_FILE = os.path.expanduser("~/.claude/.credentials.json")
CACHE_FILE = os.path.expanduser("~/.claude/quota/.usage-cache.json")

JOURS = ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim."]
MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
        "juil.", "août", "sept.", "oct.", "nov.", "déc."]

# Seuils de couleur sur le % utilisé.
SEUIL_ORANGE = 50   # >= 50 % utilisé -> orange
SEUIL_ROUGE = 80    # >= 80 % utilisé -> rouge

# Throttle anti-429 : on n'appelle l'API que si le cache est plus vieux que ça.
# L'hôte redessine la puce souvent (60 s pour SwiftBar) sans taper l'endpoint à
# chaque fois (/usage rate-limite sous rafale). Le compte à rebours reste juste :
# recalculé au rendu.
MIN_FETCH_INTERVAL = 300  # secondes


def should_skip_fetch(cache_age, force=False, min_interval=MIN_FETCH_INTERVAL):
    """True = servir le cache sans réseau (cache assez frais et pas de --force)."""
    if force or cache_age is None:
        return False
    return cache_age < min_interval


# --------------------------------------------------------------------------- token
def get_token_from_file():
    """Token OAuth depuis le fichier credentials (portable). None si absent.

    Le repli spécifique à l'OS (Keychain macOS, Credential Manager Windows) est du
    ressort du host : il appelle ceci d'abord, puis son propre fallback.
    """
    try:
        with open(CRED_FILE) as f:
            return json.load(f)["claudeAiOauth"]["accessToken"]
    except Exception:
        return None


# ----------------------------------------------------------------------------- API
def fetch(token):
    """Appelle l'endpoint /usage (non documenté). Renvoie le dict JSON."""
    req = urllib.request.Request(
        USAGE_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "anthropic-beta": "oauth-2025-04-20",
        },
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)


# ------------------------------------------------------------------------- cache
def save_cache(data, fetched_at=None):
    """Mémorise la dernière réponse OK pour servir de repli en cas d'erreur."""
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump({"fetched_at": fetched_at or time.time(), "data": data}, f)
    except Exception:
        pass


def load_cache():
    """(data, âge_en_secondes) du dernier succès, ou None si pas de cache."""
    try:
        with open(CACHE_FILE) as f:
            c = json.load(f)
        return c["data"], max(0, int(time.time() - c["fetched_at"]))
    except Exception:
        return None


# ----------------------------------------------------------------------- calculs
def used(block):
    """% utilisé d'une fenêtre de quota."""
    if not block:
        return None
    return round(block.get("utilization") or 0)


def color_for(used_pct):
    """Couleur SÉMANTIQUE selon le % utilisé. None = adaptatif (l'hôte décide du
    rendu par défaut). 'orange' >= 50 %, 'red' >= 80 %. Chaque host mappe ces noms
    à sa palette (SwiftBar les prend tels quels)."""
    if used_pct is None:
        return None
    if used_pct >= SEUIL_ROUGE:
        return "red"
    if used_pct >= SEUIL_ORANGE:
        return "orange"
    return None


def fmt_reset(iso, now=None):
    """ISO -> (compte_à_rebours, date_absolue_FR). Ex. ('4h13', 'dim. 21 juin à 06:49')."""
    when = datetime.fromisoformat(iso).astimezone()
    now = now or datetime.now(timezone.utc).astimezone()
    secs = int((when - now).total_seconds())
    if secs <= 0:
        cd = "maintenant"
    elif secs < 3600:
        cd = f"{secs // 60}m"
    elif secs < 86400:
        cd = f"{secs // 3600}h{(secs % 3600) // 60:02d}"
    else:
        cd = f"{secs // 86400}j{(secs % 86400) // 3600}h"
    absolu = f"{JOURS[when.weekday()]} {when.day} {MOIS[when.month - 1]} à {when:%H:%M}"
    return cd, absolu


def fmt_age(secs):
    """Durée écoulée compacte : '40s' / '7m' / '1h05'."""
    secs = int(secs)
    if secs < 60:
        return f"{secs}s"
    if secs < 3600:
        return f"{secs // 60}m"
    return f"{secs // 3600}h{(secs % 3600) // 60:02d}"
