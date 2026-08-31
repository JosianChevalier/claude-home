"""Host macOS — intégration OS (Keychain, LaunchAgent, notifications) + rendu SwiftBar.

Mac-only : appelle `security`, `launchctl`, `osascript`, et produit la syntaxe de
menu SwiftBar (lignes `texte | clé=valeur`). Toute la logique portable (calculs,
réseau, cache) vit dans quota_core. L'entrée SwiftBar plugin/claude-quota.1m.py
n'est qu'une coquille qui combine ce host + le cœur.
"""
import os
import subprocess
from datetime import datetime

import quota_core as core

KEYCHAIN_SERVICE = "Claude Code-credentials"

# LaunchAgent qui relance SwiftBar à l'ouverture de session.
PLIST_PATH = os.path.expanduser("~/Library/LaunchAgents/com.josian.claude-swiftbar.plist")
PLIST_LABEL = "com.josian.claude-swiftbar"


# --------------------------------------------------------------------------- token
def get_token():
    """Token OAuth : fichier credentials (cœur) d'abord, sinon Keychain macOS."""
    token = core.get_token_from_file()
    if token:
        return token
    try:
        raw = subprocess.run(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        import json
        return json.loads(raw)["claudeAiOauth"]["accessToken"]
    except Exception:
        return None


# ----------------------------------------------------------------------- rendu
def _col(used_pct):
    """Suffixe ' color=X' à coller dans une ligne SwiftBar, ou '' si adaptatif."""
    c = core.color_for(used_pct)
    return f" color={c}" if c else ""


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

    # `seven_day_sonnet` est absent des réponses de certains comptes : bloc manquant
    # = rien de consommé sur cette fenêtre, donc 0 % (et pas un « None% » affiché).
    w_use, son_use = core.used(week), core.used(son) or 0
    w_cd, w_at = core.fmt_reset(week["resets_at"], now) if week.get("resets_at") else ("?", "?")

    # Fenêtre 5h fermée : on affiche 0 % (rien ne s'accumule) et l'escargot à la
    # place du compte à rebours. Le % laissé dans le bloc appartient à une fenêtre
    # révolue — le montrer laisserait croire à une consommation en cours.
    en_cours = core.fenetre_ouverte(sess)
    if en_cours:
        s_use = core.used(sess)
        s_cd, s_at = core.fmt_reset(sess["resets_at"], now)
    else:
        s_use, s_cd, s_at = 0, core.GLYPHE_REPOS, None

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
        L.append(f"⚠ Hors-ligne — cache il y a {core.fmt_age(stale_secs)} | size=11 color=gray")
    if en_cours:
        L.append(f"Session (5h) : {s_use}% utilisé |{_col(s_use)}")
        L.append(f"-- reset dans {s_cd} · {s_at} | size=11 color=gray")
    else:
        L.append(f"Session (5h) : {core.GLYPHE_REPOS} aucune fenêtre en cours")
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
