# Rework : statusline comme source, HTTP en repli

## Contexte

`/api/oauth/usage` est agressivement rate-limité : 429 après une poignée d'appels,
blocage 30 min+, `retry-after: 0` non fiable. Poll à 30 s = throttlé le jour même ;
revenu à 5 min (23ad9da). Déjà sur main : c093ca5 (throttle bypassé au reset atteint),
bdd9d5d (reset atteint = fenêtre close, escargot, jamais « maintenant »).

Lire `README.md`, lancer `python3 tests/test_quota.py` (32 tests).

## Cible (rework, pas ajout)

| Source | Quand | Champs | Réseau |
| --- | --- | --- | --- |
| Statusline stdin `rate_limits` | chaque redessin Claude Code, toutes sessions | 5h + 7j : `used_percentage`, `resets_at` (epoch) | aucun |
| `/api/oauth/usage` | cache > 10 min (usage web/phone, laptop inactif) | idem + hebdo Fable scoped | 1 appel / 10 min max |

1. `~/.claude/statusline.py` écrit `rate_limits` + timestamp dans le cache partagé.
   Vérifié aujourd'hui : champ présent sur ce compte pour les deux fenêtres.
2. Plugin : lit le cache à chaque redessin 60 s (`.1m.` reste). Compte à rebours recalculé.
3. Repli HTTP seulement si cache > 10 min. Sur 429 : servir le cache, backoff 10 → 30 → 60 min,
   ignorer `retry-after`. État du backoff persisté dans le cache.
4. Reset atteint invalide le cache (déjà fait).
5. Menu : supprimer « Hebdo Sonnet », ajouter l'hebdo Fable : dans la réponse HTTP, entrée
   `limits[]` avec `kind: weekly_scoped` et `scope.model.display_name: Fable` (`percent`, `resets_at`).
   Absente du payload statusline → peut être périmée : afficher son âge.
6. Garder : couleurs, actions autostart/quit/refresh, UI FR, un seul cache disque.

## Tâches

- [ ] `statusline.py` : écrire `rate_limits` + timestamp (aucun changement d'affichage)
- [ ] `quota_core.py` : schéma cache (source, timestamp, backoff) ; décision fetch (frais / périmé / reset / 429)
- [ ] `macos/host.py` : ligne Fable remplace Sonnet, âge si servie par HTTP
- [ ] `macos/plugin/claude-quota.1m.py` : lecture cache, fetch selon règles
- [ ] Tests : écriture/lecture statusline, décision fetch, backoff, ligne Fable, Sonnet absent
- [ ] `README.md` : arborescence, source de la donnée, comportement
- [ ] Commit, puis `open swiftbar://refreshallplugins`
