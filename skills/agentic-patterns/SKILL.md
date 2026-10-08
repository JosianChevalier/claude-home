---
name: agentic-patterns
description: À consulter AVANT de concevoir un harnais agentique, une pipeline d'agents, une convention de KB maintenue par agents, ou un orchestrateur de workers `claude -p` (claim/release, validation, concurrence git, allowlists, watchdogs…). Catalogue de 38 patterns éprouvés — piocher avant d'inventer.
---

# agentic-patterns — catalogue de patterns

Bibliothèque de patterns réutilisables pour harness agentiques et KB maintenues par agents, dépôt public GitHub : `JosianChevalier/agentic-patterns`.

Base des URLs brutes : `https://raw.githubusercontent.com/JosianChevalier/agentic-patterns/main/`

## Protocole

1. **Charger le catalogue** (un écran, groupé par famille, une ligne par pattern : slug, problème, tags) :
   ```
   curl -sf <base>/INDEX.md
   ```
   - Vocabulaire en anglais ; chercher dans cette sortie avec les termes du domaine (`git concurrency`, pas « sérialiser dossier »).
   - Si rien ne matche, `curl -sf <base>/patterns/TAGS.md` donne le vocabulaire contrôlé des tags.
2. **Charger le pattern retenu** : `curl -sf <base>/patterns/<slug>/index.md`. Il est autoportant (problème → mécanisme → insight). Ne pas ouvrir `reference/` sauf besoin d'implémentation verbatim.
3. **Citer le slug** dans le design produit (traçabilité : le lecteur peut remonter au pattern).
