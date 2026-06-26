"""Host Windows — STUB. Même surface que host_macos, à brancher sur un hôte tray.

SwiftBar n'existe pas sur Windows : l'hôte ici n'est pas une « puce SwiftBar » mais
un tray (p.ex. pystray) ou une tâche planifiée. Tout le portable vient de quota_core ;
ce fichier ne porte QUE l'intégration Windows + un rendu adapté à son hôte.

À implémenter (chaque fonction lève NotImplementedError pour l'instant) :
  - get_token        : core.get_token_from_file() puis fallback Credential Manager / DPAPI
  - render           : sortie pour l'hôte tray (titre + tooltip + menu), PAS la syntaxe SwiftBar
  - autostart        : raccourci dans shell:startup, ou clé de registre Run
  - notify           : toast Windows (win10toast / winrt)
"""
import quota_core as core


def get_token():
    """Fichier credentials d'abord (portable), sinon fallback Windows à écrire."""
    token = core.get_token_from_file()
    if token:
        return token
    raise NotImplementedError("Fallback token Windows (Credential Manager / DPAPI) à écrire")


def render(data, *args, now=None, **kwargs):
    raise NotImplementedError("Rendu host Windows (tray) à écrire — réutiliser core.used/fmt_reset/color_for")


def render_error(msg):
    raise NotImplementedError("Rendu d'erreur host Windows à écrire")


def autostart_enabled():
    raise NotImplementedError("Autostart Windows (shell:startup / registre Run) à écrire")


def toggle_autostart():
    raise NotImplementedError("Autostart Windows (shell:startup / registre Run) à écrire")
