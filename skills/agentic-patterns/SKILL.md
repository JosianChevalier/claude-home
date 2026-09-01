---
name: agentic-patterns
description: À consulter AVANT de concevoir un harnais agentique, une pipeline d'agents, une convention de KB maintenue par agents, ou un orchestrateur de workers `claude -p` (claim/release, validation, concurrence git, allowlists, watchdogs…). Catalogue de 38 patterns éprouvés — piocher avant d'inventer.
---

# agentic-patterns — catalogue de patterns

Bibliothèque de patterns réutilisables pour harness agentiques et KB maintenues par agents : `/Users/josian/Projects/agentic-patterns` (chemin propre à cette machine).

## Protocole

1. **Requêter le catalogue** :
   ```
   /Users/josian/Projects/agentic-patterns/piocher.py <termes>
   ```
   - Tous les termes doivent matcher (substring, case-insensitive) sur slug, tags, description ou corps.
   - **Termes en anglais** (le catalogue est indexé en anglais : `git concurrency`, pas « sérialiser dossier »).
   - `--tags` liste le vocabulaire contrôlé (source : `patterns/TAGS.md`) — point de départ si les termes libres ne matchent rien.
2. **Charger le pattern retenu** : `patterns/<slug>/index.md`. Il est autoportant (problème → mécanisme → insight). Ne pas ouvrir `reference/` sauf besoin d'implémentation verbatim.
3. **Citer le slug** dans le design produit (traçabilité : le lecteur peut remonter au pattern).
