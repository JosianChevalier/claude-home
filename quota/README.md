# Puce quota Claude Code (SwiftBar)

Affiche dans la barre de menu macOS l'état de la session Claude Code :
**% utilisé** de la fenêtre courante + **temps avant reset**. Détail au clic.

```
23% · 4h05            ← % utilisé (session 5h) · compte à rebours reset
```

## Arborescence (`~/.claude/quota/`)

```
quota_core.py          cœur PORTABLE — calculs, /usage, cache, throttle, token-fichier. Zéro OS.
macos/
  host.py              host macOS — Keychain, LaunchAgent, notif osascript + rendu SwiftBar
  plugin/
    claude-quota.1m.py entrée SwiftBar (coquille = core + macos/host). 1m = redessin 60 s.
windows/
  host.py              host Windows (stub) — même surface, à brancher sur un tray
tests/test_quota.py    24 tests stdlib. python3 tests/test_quota.py
README.md
.usage-cache.json      dernière réponse OK (repli + throttle). Auto-généré, jetable, gitignored.
```

Séparation en deux axes : **(1)** le `.py` exécuté par SwiftBar ne fait qu'orchestrer
(token, fetch, print) ; la logique vit dans les modules, testable sans réseau ni SwiftBar.
**(2)** le portable (`quota_core`) est isolé de l'OS-spécifique (`macos/`, `windows/`) — un
futur host Windows réutilise le cœur tel quel.

**Pourquoi `plugin/` isolé sous `macos/`.** SwiftBar fait une icône de **chaque fichier** de
son `PluginDirectory` (récursivement). Mettre `host.py` à côté du plugin = icône parasite
cassée. Donc `PluginDirectory` pointe sur `macos/plugin/` qui ne contient **que** le plugin ;
`macos/host.py` (un cran au-dessus) et `quota_core.py` (deux crans) sont hors scan, importés
via `sys.path`. Réglé une fois dans les `defaults` SwiftBar (`PluginDirectory`).

## Source de la donnée

Endpoint OAuth **non documenté** (= ce que fait `/usage`) :

```bash
curl -s https://api.anthropic.com/api/oauth/usage \
  -H "Authorization: Bearer $TOKEN" \
  -H "anthropic-beta: oauth-2025-04-20"
```

- **Token** : `~/.claude/.credentials.json` sinon Keychain (`security find-generic-password -s "Claude Code-credentials" -w`). Sur ce Mac → Keychain.
- **Réponse** : `five_hour` / `seven_day` / `seven_day_sonnet`, chacun `{utilization (%), resets_at (ISO)}`. `*_dollars` = `null` (abonnement au quota, pas au crédit $).
- ⚠️ Non documenté = **peut casser sans préavis**. La puce dégrade proprement (cache, puis `⚠ Claude` rouge).

## Comportement

- Couleur du **texte** (pas de pastille) : adaptatif < 50 % utilisé, **orange ≥ 50 %**, **rouge ≥ 80 %**. La barre suit la fenêtre affichée (session 5h). Seuils = `SEUIL_ORANGE` / `SEUIL_ROUGE` dans `quota_core`.
- **Throttle anti-429** : la puce est redessinée toutes les 60 s, mais l'API n'est appelée que si le cache dépasse `MIN_FETCH_INTERVAL` (300 s) — sinon on ré-affiche le cache **sans réseau** (le compte à rebours, lui, est recalculé à chaque rendu, donc juste). Évite les rafales sur `/usage` (qui rate-limite, surtout cumulé aux appels de Claude Code lui-même). Le bouton *Rafraîchir* force un vrai appel (`--force`).
- **Cache** : succès → écrit `.usage-cache.json`. Erreur/429/token absent → réaffiche la dernière valeur **grisée + `⋯`** avec son âge (« cache il y a Xm »).
- **Menu déroulant** : session 5h, hebdo 7j, hebdo Sonnet (% utilisé + reset compte à rebours ET heure absolue FR) ; toggle *Lancer au démarrage* ; *Quitter* ; *Rafraîchir*.
- **Démarrage auto** : LaunchAgent `~/Library/LaunchAgents/com.josian.claude-swiftbar.plist` (`open -gja SwiftBar`, RunAtLoad). Le toggle le crée/charge ou le retire (`launchctl load/unload -w`) + notif macOS.

## Gotchas (déjà rencontrés)

- **Actions cliquables** : SwiftBar ne résout PAS le shebang `env python3` au clic quand python vit dans Homebrew. → on **embarque `sys.executable`** dans `bash=…`. Si tu changes d'interpréteur, rien à faire (calculé au runtime).
- **`429`** : à force d'appels rapprochés l'endpoint rate-limite. 60 s en régime normal suffit ; chaque *Rafraîchir* = 1 appel de plus.
- **Couleur en mode clair** : on évite `white` fixe (invisible). État sain = pas de `color=` → SwiftBar adapte (noir/blanc selon thème).

## Itérer

1. Logique portable → `quota_core.py` ; rendu/intégration mac → `macos/host.py`.
2. `python3 tests/test_quota.py` (rapide, hors-ligne via fixture `SAMPLE`).
3. `./macos/plugin/claude-quota.1m.py` pour voir le rendu SwiftBar brut.
4. `open swiftbar://refreshallplugins` pour rafraîchir la puce sans attendre.

Changer le **redessin** = renommer le fichier (`.30s.` / `.1m.` / `.5m.`). Changer la
fréquence des **appels API** = `MIN_FETCH_INTERVAL` dans `quota_core` (indépendant du redessin).
Format des lignes SwiftBar : `Titre | color= size= bash= param1= terminal= refresh=`.

## Portabilité (Windows)

SwiftBar est macOS-only : pas de portage Windows du plugin lui-même. Le cœur
(`quota_core.py`) est lui 100 % portable. Pour Windows, implémenter `windows/host.py`
(token via Credential Manager, autostart via `shell:startup`, notif toast, rendu pour
un tray type `pystray`) + une entrée qui combine `quota_core` + `windows/host`.
