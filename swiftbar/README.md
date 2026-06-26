# Puce quota Claude Code (SwiftBar)

Affiche dans la barre de menu macOS l'état de la session Claude Code :
**% utilisé** de la fenêtre courante + **temps avant reset**. Détail au clic.

```
23% · 4h05            ← % utilisé (session 5h) · compte à rebours reset
```

## Fichiers (`~/.claude/swiftbar/`)

| Fichier | Rôle |
|---|---|
| `plugin/claude-quota.1m.py` | plugin SwiftBar (coquille fine). Le `1m` = redessin 60 s, encodé dans le nom. **Seul dans `plugin/`** (voir ci-dessous). |
| `claude_quota_lib.py` | **toute la logique** (calculs, rendu, cache, throttle, démarrage auto). Importable, testée. |
| `test_claude_quota.py` | 23 tests stdlib (`unittest`). `python3 test_claude_quota.py`. |
| `.usage-cache.json` | dernière réponse OK (repli + source du throttle). Auto-généré, jetable. |

Séparation voulue : le `.py` exécuté par SwiftBar ne fait qu'I/O (token, fetch, print).
Tout le reste vit dans `_lib` pour être testable sans réseau ni SwiftBar.

**Pourquoi `plugin/` à part.** SwiftBar fait une icône de **chaque fichier** de son
dossier de plugins (récursivement). Lib + tests dans le même dossier = icônes
parasites. Donc `PluginDirectory` pointe sur `plugin/` qui ne contient **que** le
plugin ; la lib (un cran au-dessus) est hors scan. Le plugin l'importe via le
dossier parent. Réglé une fois dans les `defaults` SwiftBar (`PluginDirectory`).

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

- Couleur du **texte** (pas de pastille) : adaptatif < 50 % utilisé, **orange ≥ 50 %**, **rouge ≥ 80 %**. La barre prend le pire des deux fenêtres (session/hebdo). Seuils = `SEUIL_ORANGE` / `SEUIL_ROUGE` dans `_lib`.
- **Throttle anti-429** : la puce est redessinée toutes les 60 s, mais l'API n'est appelée que si le cache dépasse `MIN_FETCH_INTERVAL` (300 s) — sinon on ré-affiche le cache **sans réseau** (le compte à rebours, lui, est recalculé à chaque rendu, donc juste). Évite les rafales sur `/usage` (qui rate-limite, surtout cumulé aux appels de Claude Code lui-même). Le bouton *Rafraîchir* force un vrai appel (`--force`).
- **Cache** : succès → écrit `.usage-cache.json`. Erreur/429/token absent → réaffiche la dernière valeur **grisée + `⋯`** avec son âge (« cache il y a Xm »).
- **Menu déroulant** : session 5h, hebdo 7j, hebdo Sonnet (% utilisé + reset compte à rebours ET heure absolue FR) ; toggle *Lancer au démarrage* ; *Quitter* ; *Rafraîchir*.
- **Démarrage auto** : LaunchAgent `~/Library/LaunchAgents/com.josian.claude-swiftbar.plist` (`open -gja SwiftBar`, RunAtLoad). Le toggle le crée/charge ou le retire (`launchctl load/unload -w`) + notif macOS.

## Gotchas (déjà rencontrés)

- **Actions cliquables** : SwiftBar ne résout PAS le shebang `env python3` au clic quand python vit dans Homebrew. → on **embarque `sys.executable`** dans `bash=…`. Si tu changes d'interpréteur, rien à faire (calculé au runtime).
- **`429`** : à force d'appels rapprochés l'endpoint rate-limite. 60 s en régime normal suffit ; chaque *Rafraîchir* = 1 appel de plus.
- **Couleur en mode clair** : on évite `white` fixe (invisible). État sain = pas de `color=` → SwiftBar adapte (noir/blanc selon thème).

## Itérer

1. Modifier `claude_quota_lib.py` (logique) — c'est là que tout se passe.
2. `python3 test_claude_quota.py` (rapide, hors-ligne via fixture `SAMPLE`).
3. `./plugin/claude-quota.1m.py` pour voir le rendu SwiftBar brut.
4. `open swiftbar://refreshallplugins` pour rafraîchir la puce sans attendre.

Changer le **redessin** = renommer le fichier (`.30s.` / `.1m.` / `.5m.`). Changer la
fréquence des **appels API** = `MIN_FETCH_INTERVAL` dans `_lib` (indépendant du redessin).
Format des lignes SwiftBar : `Titre | color= size= bash= param1= terminal= refresh=`.
```
