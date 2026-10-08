"""Cœur PORTABLE du plugin quota Claude Code — calculs et formatage, rien d'autre.

ZÉRO I/O, zéro OS : d'où vient la donnée (status line, HTTP, cache) est l'affaire de
providers.py ; comment elle s'affiche (SwiftBar, tray) celle d'un host. N'importe quel
host importe ce module pour la logique. Couvert par test_quota.py.
"""
from datetime import datetime, timezone

JOURS = ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim."]
MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
        "juil.", "août", "sept.", "oct.", "nov.", "déc."]

# Seuils de couleur sur le % utilisé.
SEUIL_ORANGE = 50   # >= 50 % utilisé -> orange
SEUIL_ROUGE = 80    # >= 80 % utilisé -> rouge

# Tient la place du compte à rebours quand aucune fenêtre n'est ouverte : rien ne
# tourne, donc rien à décompter. Un escargot plutôt qu'une horloge vide — l'absence
# de fenêtre n'est pas une attente, et la puce ne doit pas pousser à s'y remettre.
GLYPHE_REPOS = "🐌"

# ----------------------------------------------------------------------- calculs
def used(block):
    """% utilisé d'une fenêtre de quota."""
    if not block:
        return None
    return round(block.get("utilization") or 0)


def fenetre_ouverte(block, now=None):
    """True si la fenêtre a une échéance À VENIR — donc quelque chose à décompter.

    L'API renvoie des blocs `{utilization: x, resets_at: null}` : un quota sans
    échéance. Pas d'échéance, ou échéance atteinte = pas de fenêtre en cours ; le %
    qui traîne dedans appartient à une fenêtre déjà close et ne mesure plus rien.
    """
    iso = (block or {}).get("resets_at")
    if not iso:
        return False
    now = now or datetime.now(timezone.utc)
    return datetime.fromisoformat(iso) > now


def echeance_passee(data, now=None):
    """True si la fenêtre 5h de l'instantané a atteint son reset : la donnée est
    périmée par construction (nouvelle fenêtre côté API), quel que soit son âge."""
    block = (data or {}).get("five_hour") or {}
    return bool(block.get("resets_at")) and not fenetre_ouverte(block, now)


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
