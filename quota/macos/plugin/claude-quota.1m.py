#!/usr/bin/env python3
"""SwiftBar plugin — état de la session Claude Code (quota restant + reset).

Source : endpoint OAuth non documenté api.anthropic.com/api/oauth/usage (= /usage).
Refresh affiché : 60 s (encodé dans le nom). Mais l'API n'est interrogée qu'au-delà
de MIN_FETCH_INTERVAL (throttle anti-429) : entre deux, on ré-affiche le cache —
le compte à rebours, lui, est recalculé à chaque rendu donc reste juste.

Coquille fine : la logique portable vit dans quota_core, l'intégration mac + le
rendu SwiftBar dans host_macos (tous deux dans le dossier parent, testés).

Ce fichier est SEUL dans son dossier : SwiftBar scanne le dossier de plugins
(récursivement) et fait une icône de chaque fichier. La lib et les tests vivent
donc un cran au-dessus, hors du dossier scanné.

Actions cliquables (passées par SwiftBar en argv) :
  --toggle-autostart  active/désactive le lancement de SwiftBar au démarrage
  --quit              quitte SwiftBar (ferme la puce)
  --force             force un appel API (bypass throttle) — bouton Rafraîchir
"""
import os
import subprocess
import sys

# Ce fichier est isolé dans macos/plugin/ (SwiftBar scanne CE dossier).
# host vit dans macos/ (parent) ; quota_core à la racine quota/ (grand-parent).
_PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))   # quota/macos/plugin
_MACOS_DIR = os.path.dirname(_PLUGIN_DIR)                   # quota/macos
_QUOTA_DIR = os.path.dirname(_MACOS_DIR)                    # quota
sys.path.insert(0, _QUOTA_DIR)
sys.path.insert(0, _MACOS_DIR)
import quota_core as core
import host

SELF = os.path.abspath(__file__)


def main():
    if "--toggle-autostart" in sys.argv:
        host.toggle_autostart()
        return
    if "--quit" in sys.argv:
        subprocess.run(["osascript", "-e", 'quit app "SwiftBar"'])
        return

    force = "--force" in sys.argv
    auto = host.autostart_enabled()
    cached = core.load_cache()

    # Throttle : cache assez frais (et pas de --force) -> on l'affiche sans réseau.
    # stale_secs=None : c'est récent, pas une donnée périmée, donc pas de gris/⋯.
    if cached and core.should_skip_fetch(cached[1], force):
        print(host.render(cached[0], SELF, sys.executable, autostart_on=auto))
        return

    def stale_or_error(msg):
        if cached:
            data, age = cached
            print(host.render(data, SELF, sys.executable, autostart_on=auto, stale_secs=age))
        else:
            print(host.render_error(msg))

    token = host.get_token()
    if not token:
        stale_or_error("Token introuvable (fichier credentials ou Keychain)")
        return
    try:
        data = core.fetch(token)
    except Exception as e:
        stale_or_error(f"Erreur API : {e}")
        return
    core.save_cache(data)
    print(host.render(data, SELF, sys.executable, autostart_on=auto))


if __name__ == "__main__":
    main()
