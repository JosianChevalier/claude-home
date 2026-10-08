# Puce quota Claude Code (SwiftBar)

Affiche dans la barre de menu macOS l'état de la session Claude Code :
**% utilisé** de la fenêtre courante + **temps avant reset**. Détail au clic.

```
23% · 4h05            ← % utilisé (session 5h) · compte à rebours reset
 0% · 🐌              ← aucune fenêtre en cours (rien ne tourne, rien à décompter)
```

## Arborescence (`~/.claude/quota/`)

```
quota_core.py          cœur PORTABLE — calculs et formatage. Zéro I/O, zéro OS.
providers.py           sources PORTABLES (SPI) — port Snapshot, StatusLine, Http, Fallback.
macos/
  host.py              host macOS — Keychain, LaunchAgent, notif osascript + rendu SwiftBar
  plugin/
    claude-quota.10s.py entrée SwiftBar (coquille = core + macos/host). 10s = redessin 10 s.
windows/
  host.py              host Windows (stub) — même surface, à brancher sur un tray
tests/test_quota.py    39 tests stdlib. python3 tests/test_quota.py
README.md
.statusline-snapshot.json  rate_limits déposé par ~/.claude/statusline.py. Jetable, gitignored.
.usage-cache.json          dernière réponse HTTP OK. Jetable, gitignored.
```

Hexagonal : **(1)** le `.py` exécuté par SwiftBar ne fait que composer (sources → rendu) ;
la logique vit dans les modules, testable sans réseau ni SwiftBar. **(2)** le portable
(`quota_core`, `providers`) est isolé de l'OS-spécifique (`macos/`, `windows/`) — un futur
host Windows réutilise le cœur tel quel. **(3)** la donnée arrive par un port
(`get() -> Snapshot(data, fetched_at)`) : le rendu ignore si elle vient de la status line
ou de l'API.

**Pourquoi `plugin/` isolé sous `macos/`.** SwiftBar fait une icône de **chaque fichier** de
son `PluginDirectory` (récursivement). Mettre `host.py` à côté du plugin = icône parasite
cassée. Donc `PluginDirectory` pointe sur `macos/plugin/` qui ne contient **que** le plugin ;
`macos/host.py` (un cran au-dessus) et `quota_core.py` (deux crans) sont hors scan, importés
via `sys.path`. Réglé une fois dans les `defaults` SwiftBar (`PluginDirectory`).

## Sources de la donnée (`providers.py`)

1. **Status line** (gratuit, primaire). Claude Code passe `rate_limits` (`five_hour` /
   `seven_day` : `used_percentage`, `resets_at` epoch) à `~/.claude/statusline.py` à chaque
   requête ; celle-ci le dépose brut dans `.statusline-snapshot.json`. L'adaptateur
   `StatusLine` le normalise au format `/usage`. Claude Code retire une fenêtre dès son reset.
2. **HTTP** (repli). Endpoint OAuth **non documenté** (= ce que fait `/usage`) :

```bash
curl -s https://api.anthropic.com/api/oauth/usage \
  -H "Authorization: Bearer $TOKEN" \
  -H "anthropic-beta: oauth-2025-04-20"
```

- **Token** : `~/.claude/.credentials.json` sinon Keychain (`security find-generic-password -s "Claude Code-credentials" -w`). Sur ce Mac → Keychain.
- **Réponse** : `five_hour` / `seven_day` / `seven_day_sonnet`, chacun `{utilization (%), resets_at (ISO)}`. `*_dollars` = `null` (abonnement au quota, pas au crédit $).
- ⚠️ Non documenté = **peut casser sans préavis**. La puce dégrade proprement (repli, puis `⚠ Claude` rouge).

**`Fallback`** : l'instantané le plus frais gagne (status line ou cache HTTP). L'API n'est
appelée que s'il a **`STALE_AFTER` (10 min)** ou plus, si le reset de session est atteint, ou
sur `--force`. Tant qu'on travaille dans Claude Code, zéro appel réseau.

## Comportement

- Couleur du **texte** (pas de pastille) : adaptatif < 50 % utilisé, **orange ≥ 50 %**, **rouge ≥ 80 %**. La barre suit la fenêtre affichée (session 5h). Seuils = `SEUIL_ORANGE` / `SEUIL_ROUGE` dans `quota_core`.
- **Throttle anti-429** = `STALE_AFTER` : la puce est redessinée toutes les 10 s (lecture fichier, zéro réseau), mais après un appel HTTP, OK **ou échoué**, pas d'appel avant 10 min (le compte à rebours, lui, est recalculé à chaque rendu, donc juste). Exception : reset de la session atteint → appel immédiat, sinon la puce resterait sur « maintenant ». Le bouton *Rafraîchir* force un vrai appel (`--force`).
- **Fenêtre fermée** : l'API peut renvoyer `five_hour` sans `resets_at` (ou `null`), ou avec un `resets_at` déjà atteint. Pas d'échéance à venir = pas de fenêtre en cours ; le % qui traîne dedans appartient à une fenêtre révolue et ne mesure plus rien. La puce affiche alors `0% · 🐌`, sans couleur — l'absence de fenêtre n'est pas une attente, la puce ne doit pas pousser à s'y remettre. Prédicat `fenetre_ouverte()` + `GLYPHE_REPOS` dans `quota_core`.
- **Repli** : succès HTTP → écrit `.usage-cache.json`. Erreur/429/token absent → réaffiche l'instantané le plus frais **grisé + `⋯`** avec son âge (« cache il y a Xm »).
- **Menu déroulant** : session 5h, hebdo 7j (% utilisé + reset compte à rebours ET heure absolue FR) ; toggle *Lancer au démarrage* ; *Quitter* ; *Rafraîchir*.
- **Démarrage auto** : LaunchAgent `~/Library/LaunchAgents/com.josian.claude-swiftbar.plist` (`open -gja SwiftBar`, RunAtLoad). Le toggle le crée/charge ou le retire (`launchctl load/unload -w`) + notif macOS.

## Gotchas (déjà rencontrés)

- **Actions cliquables** : SwiftBar ne résout PAS le shebang `env python3` au clic quand python vit dans Homebrew. → on **embarque `sys.executable`** dans `bash=…`. Si tu changes d'interpréteur, rien à faire (calculé au runtime).
- **`429`** : à force d'appels rapprochés l'endpoint rate-limite. En régime normal la status line nourrit la puce et l'API n'est jamais appelée ; chaque *Rafraîchir* = 1 appel.
- **Couleur en mode clair** : on évite `white` fixe (invisible). État sain = pas de `color=` → SwiftBar adapte (noir/blanc selon thème).

## Itérer

1. Calculs → `quota_core.py` ; sources → `providers.py` ; rendu/intégration mac → `macos/host.py`.
2. `python3 tests/test_quota.py` (rapide, hors-ligne via fixture `SAMPLE`).
3. `./macos/plugin/claude-quota.10s.py` pour voir le rendu SwiftBar brut.
4. `open swiftbar://refreshallplugins` pour rafraîchir la puce sans attendre.

Changer le **redessin** = renommer le fichier (`.10s.` / `.30s.` / `.1m.`). Changer le seuil de
**péremption / appels API** = `STALE_AFTER` dans `providers` (indépendant du redessin).
Format des lignes SwiftBar : `Titre | color= size= bash= param1= terminal= refresh=`.

## Portabilité (Windows)

SwiftBar est macOS-only : pas de portage Windows du plugin lui-même. Le cœur
(`quota_core.py`, `providers.py`) est lui 100 % portable. Pour Windows, implémenter `windows/host.py`
(token via Credential Manager, autostart via `shell:startup`, notif toast, rendu pour
un tray type `pystray`) + une entrée qui combine `quota_core` + `windows/host`.
