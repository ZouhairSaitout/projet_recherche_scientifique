# Projet Recherche Scientifique — Profondeur des réseaux de neurones

**Cours :** Initiation à la recherche scientifique  
**Groupe :** Zouhair Saitout, Thibaud Crotta, Romain Ben  
**Deadline :** Mardi 13 mai 2026

---

## Question de recherche

> Peut-on caractériser mathématiquement la classe des fonctions pour lesquelles la
> profondeur d'un réseau de neurones est strictement nécessaire, c'est-à-dire celles
> dont l'approximation par un réseau peu profond requiert un nombre de neurones
> exponentiellement plus grand ?

---

## Répartition du travail

| Responsable | Rapport (sections) | Slides | Oral (approx.) |
|---|---|---|---|
| **Romain** | 1 (Intro) + 5 (Conclusion) + structure LaTeX + biblio | 1–5 & 15–16 | ~5 min |
| **Zouhair** | 2 (Formalisme) + 3a (Telgarsky, Montufar) | 6–10 | ~4.5 min |
| **Thibaud** | 3b (Eldan-Shamir) + 4 (Caractérisation) | 11–14 | ~4.5 min |

---

## Plan du rapport

### Section 1 — Introduction et contexte (Romain) ✅
- Contexte : shallow vs deep en pratique
- Théorème d'approximation universelle : Cybenko (1989), Hornik (1991)
- Bornes quantitatives : Barron (1993)
- La question du coût en neurones et la problématique

### Section 2 — Formalisme mathématique (Zouhair) 🔲
- Définitions : réseau de neurones, profondeur $L$, largeur $W$, $\varepsilon$-approximation
- Activations : sigmoïde, ReLU
- Classes de fonctions : $\mathcal{C}^k$, espaces de Sobolev
- Sources : Pinkus (1999), Yarotsky (2017)

### Section 3 — Résultats de séparation par profondeur (Zouhair + Thibaud) 🔲
**Zouhair :**
- Telgarsky (2016) : fonctions zigzag, séparation exponentielle entre profondeur $k$ et $\lfloor k/2 \rfloor$
- Montufar et al. (2014) : nombre de régions linéaires, croissance exponentielle avec la profondeur

**Thibaud :**
- Eldan & Shamir (2016) : fonctions radiales, séparation 2 couches vs 3 couches

### Section 4 — Vers une caractérisation mathématique (Thibaud) 🔲
- Daniely (2017) : séparation depth-2 vs depth-3 via polynômes de bas degré
- Safran & Shamir (2017) : trade-offs profondeur-largeur pour fonctions naturelles
- Raghu et al. (2017) : longueur de trajectoire comme mesure d'expressivité
- Diakonikolas et al. (2022) : caractérisation par spectre de Fourier sphérique
- Vardi et al. (2020) : barrières formelles aux preuves de séparation

### Section 5 — Conclusion et questions ouvertes (Romain) ✅
- Bilan des résultats de séparation prouvés
- Barrières formelles (Vardi et al. 2020)
- Perspectives : Fourier sphérique, théorie de la complexité, implications pratiques

---

## Bibliographie (13 références)

| Fichier | Référence |
|---|---|
| `Cybenko1989.pdf` | Cybenko, G. (1989). *Approximation by superpositions of a sigmoidal function.* Math. Control Signals Syst. |
| `93.Barron.Universal.pdf` | Barron, A.R. (1993). *Universal approximation bounds for superpositions of a sigmoidal function.* IEEE Trans. Inf. Theory. |
| `approximation_capabilities_of_...pdf` | Hornik, K. (1991). *Approximation capabilities of multilayer feedforward networks.* Neural Networks. |
| `approximation-theory-of-the-mlp-...pdf` | Pinkus, A. (1999). *Approximation theory of the MLP model in neural networks.* Acta Numerica. |
| `1402.pdf` | Montufar, G. et al. (2014). *On the number of linear regions of deep neural networks.* NeurIPS. |
| `eldan16.pdf` | Eldan, R. & Shamir, O. (2016). *The power of depth for feedforward neural networks.* COLT. |
| `telgarsky16.pdf` | Telgarsky, M. (2016). *Benefits of depth in neural networks.* COLT. |
| `1606.pdf` | Raghu, M. et al. (2017). *On the expressive power of deep neural networks.* ICML. |
| `daniely17a.pdf` | Daniely, A. (2017). *Depth separation for neural networks.* COLT. |
| `safran17a.pdf` | Safran, I. & Shamir, O. (2017). *Depth-width tradeoffs in approximating natural functions.* ICML. |
| `error_vounds_for_...pdf` | Yarotsky, D. (2017). *Error bounds for approximations with deep ReLU networks.* Neural Networks. |
| `e1fe6165...pdf` | Vardi, G., Yehudai, G. & Shamir, O. (2020). *Neural networks with small weights and depth-separation barriers.* NeurIPS. |
| `21-1109.pdf` | Diakonikolas, I. et al. (2022). *Depth separation beyond radial functions.* JMLR. |

---

## Structure du repo

```
/
├── rapport/
│   ├── main.tex          # Source LaTeX principale
│   └── biblio.bib        # Références BibTeX
├── slides/
│   ├── slides_romain.md  # Contenu slides Romain ✅
│   ├── slides_zouhair.md # TODO Zouhair
│   └── slides_thibaud.md # TODO Thibaud
├── script/
│   ├── script_romain.md  # Script oral Romain ✅
│   ├── script_zouhair.md # TODO Zouhair
│   └── script_thibaud.md # TODO Thibaud
├── biblio/               # 13 PDFs des articles
└── README.md
```

---

## Workflow Git

Branches individuelles, merge sur `main` après relecture croisée :
- `romain/rapport` — sections 1 & 5, structure LaTeX
- `zouhair/rapport` — sections 2 & 3a
- `thibaud/rapport` — sections 3b & 4
