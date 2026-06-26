"""Logique du plugin SwiftBar « quota Claude Code » — importable et testable.

Le plugin SwiftBar (plugin/claude-quota.1m.py) n'est qu'une coquille au-dessus d'ici :
récupération token + appel API + impression. Toute la logique pure (calculs,
formatage, rendu, démarrage auto) vit ici pour être couverte par les tests.
"""
import json
import os
import subprocess
import time
import urllib.request
from datetime import datetime, timezone

USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
CRED_FILE = os.path.expanduser("~/.claude/.credentials.json")
KEYCHAIN_SERVICE = "Claude Code-credentials"
CACHE_FILE = os.path.expanduser("~/.claude/swiftbar/.usage-cache.json")

# LaunchAgent qui relance SwiftBar à l'ouverture de session.
PLIST_PATH = os.path.expanduser("~/Library/LaunchAgents/com.josian.claude-swiftbar.plist")
PLIST_LABEL = "com.josian.claude-swiftbar"

JOURS = ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim."]
MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
        "juil.", "août", "sept.", "oct.", "nov.", "déc."]

# Seuils de couleur sur le % utilisé.
SEUIL_ORANGE = 50   # >= 50 % utilisé -> orange
SEUIL_ROUGE = 80    # >= 80 % utilisé -> rouge

# Throttle anti-429 : on n'appelle l'API que si le cache est plus vieux que ça.
# SwiftBar redessine la puce toutes les 60 s, mais sans taper l'endpoint à chaque
# fois (l'endpoint /usage rate-limite sous rafale, surtout cumulé aux appels que
# Claude Code lui-même fait). Le compte à rebours reste juste : recalculé au rendu.
MIN_FETCH_INTERVAL = 300  # secondes


def should_skip_fetch(cache_age, force=False, min_interval=MIN_FETCH_INTERVAL):
    """True = servir le cache sans réseau (cache assez frais et pas de --force)."""
    if force or cache_age is None:
        return False
    return cache_age < min_interval


# --------------------------------------------------------------------------- I/O
def get_token():
    """Token OAuth : fichier credentials d'abord, sinon Keychain macOS."""
    try:
        with open(CRED_FILE) as f:
            return json.load(f)["claudeAiOauth"]["accessToken"]
    except Exception:
        pass
    try:
        raw = subprocess.run(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        return json.loads(raw)["claudeAiOauth"]["accessToken"]
    except Exception:
        return None


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
    """Couleur du texte selon le % utilisé. None = adaptative (défaut SwiftBar :
    noir en mode clair, blanc en mode sombre). Orange >= 50 %, rouge >= 80 %."""
    if used_pct is None:
        return None
    if used_pct >= SEUIL_ROUGE:
        return "red"
    if used_pct >= SEUIL_ORANGE:
        return "orange"
    return None


def _col(used_pct):
    """Suffixe ' color=X' à coller dans une ligne SwiftBar, ou '' si adaptatif."""
    c = color_for(used_pct)
    return f" color={c}" if c else ""


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


# ----------------------------------------------------------------------- rendu
def render(data, plugin_path, python_exec, now=None, autostart_on=False, stale_secs=None):
    """Construit la sortie SwiftBar complète (barre + menu déroulant).

    python_exec = chemin exact de l'interpréteur (sys.executable), embarqué dans
    les actions cliquables : SwiftBar ne résout pas le shebang `env python3` au clic
    quand python vit dans Homebrew.
    stale_secs != None = données servies depuis le cache (API injoignable) : la
    barre passe en gris et une ligne signale l'âge.
    """
    sess = data.get("five_hour") or {}
    week = data.get("seven_day") or {}
    son = data.get("seven_day_sonnet") or {}

    s_use, w_use, son_use = used(sess), used(week), used(son)
    s_cd, s_at = fmt_reset(sess["resets_at"], now) if sess.get("resets_at") else ("?", "?")
    w_cd, w_at = fmt_reset(week["resets_at"], now) if week.get("resets_at") else ("?", "?")

    # Barre de menu : couleur calée sur la fenêtre AFFICHÉE (session 5h) — le %
    # montré et la couleur parlent de la même chose. L'hebdo reste haut des jours
    # durant en fin de semaine sans qu'on la dépasse : le colorer affolerait la
    # puce pour rien. (Alerte hebdo = futur badge dédié, pas la couleur du texte.)
    # En mode cache (stale), on force le gris pour signaler la péremption.
    if stale_secs is None:
        L = [f"{s_use}% · {s_cd} | size=13{_col(s_use)}"]
    else:
        L = [f"{s_use}% · {s_cd} ⋯ | size=13 color=gray"]

    L.append("---")
    L.append("Claude Code — quota | size=11 color=gray")
    if stale_secs is not None:
        L.append(f"⚠ Hors-ligne — cache il y a {fmt_age(stale_secs)} | size=11 color=gray")
    L.append(f"Session (5h) : {s_use}% utilisé |{_col(s_use)}")
    L.append(f"-- reset dans {s_cd} · {s_at} | size=11 color=gray")
    L.append(f"Hebdo (7j) : {w_use}% utilisé |{_col(w_use)}")
    L.append(f"-- reset dans {w_cd} · {w_at} | size=11 color=gray")
    L.append(f"Hebdo Sonnet : {son_use}% utilisé | size=11 color=gray")

    L.append("---")
    act = f"bash={python_exec} param1={plugin_path}"
    coche = "✓" if autostart_on else "✗"
    L.append(f"{coche} Lancer au démarrage | {act} param2=--toggle-autostart "
             f"terminal=false refresh=true")
    L.append(f"Quitter SwiftBar | {act} param2=--quit terminal=false")
    L.append(f"Rafraîchir | {act} param2=--force terminal=false refresh=true")
    when = (now or datetime.now()).astimezone()
    L.append(f"Maj {when:%H:%M:%S} | size=11 color=gray")
    return "\n".join(L)


def render_error(msg):
    """Sortie SwiftBar dégradée (texte rouge) en cas d'échec."""
    return f"⚠ Claude | color=red\n---\n{msg}\nRafraîchir | refresh=true"


# ------------------------------------------------------------------ démarrage auto
def autostart_enabled():
    return os.path.exists(PLIST_PATH)


def _plist_xml():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>{PLIST_LABEL}</string>
  <key>ProgramArguments</key>
  <array><string>/usr/bin/open</string><string>-gja</string><string>SwiftBar</string></array>
  <key>RunAtLoad</key><true/>
</dict>
</plist>
"""


def enable_autostart():
    os.makedirs(os.path.dirname(PLIST_PATH), exist_ok=True)
    with open(PLIST_PATH, "w") as f:
        f.write(_plist_xml())
    subprocess.run(["launchctl", "load", "-w", PLIST_PATH], capture_output=True)


def disable_autostart():
    subprocess.run(["launchctl", "unload", "-w", PLIST_PATH], capture_output=True)
    try:
        os.remove(PLIST_PATH)
    except FileNotFoundError:
        pass


def _notify(msg):
    subprocess.run(["osascript", "-e",
                    f'display notification "{msg}" with title "Claude Code quota"'],
                   capture_output=True)


def toggle_autostart():
    if autostart_enabled():
        disable_autostart()
        _notify("Lancement au démarrage désactivé")
    else:
        enable_autostart()
        _notify("Lancement au démarrage activé")
