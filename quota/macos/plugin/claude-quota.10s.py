#!/usr/bin/env python3
"""SwiftBar plugin — état de la session Claude Code (quota restant + reset).

Sources (providers.py) : l'instantané déposé par la status line à chaque requête
Claude Code, sinon l'endpoint /usage quand tout est périmé (STALE_AFTER).
Redessin : 10 s (encodé dans le nom). Pull sans réseau : on relit l'instantané et on
recalcule le compte à rebours ; la donnée ne bouge que quand la status line la dépose.

Coquille fine : la logique portable vit dans quota_core + providers, l'intégration
mac + le rendu SwiftBar dans macos/host (tous testés).

Ce fichier est SEUL dans son dossier : SwiftBar scanne le dossier de plugins
(récursivement) et fait une icône de chaque fichier. La lib et les tests vivent
donc un cran au-dessus, hors du dossier scanné.

Actions cliquables (passées par SwiftBar en argv) :
  --toggle-autostart  active/désactive le lancement de SwiftBar au démarrage
  --quit              quitte SwiftBar (ferme la puce)
  --force             force un appel API (bypass fraîcheur) — bouton Rafraîchir
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
import host
import providers

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
    source = providers.Fallback(providers.StatusLine(), http=providers.Http(host.get_token))

    snap, err = source.get(force)
    if snap is None:
        print(host.render_error(err))
    else:
        stale = providers.age(snap) if err else None   # repli après échec -> gris + âge
        print(host.render(snap.data, SELF, sys.executable, autostart_on=auto, stale_secs=stale))


if __name__ == "__main__":
    main()
