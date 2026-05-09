# Slides — Romain Ben
# Slides 1–5 (Introduction) + Slide 15–16 (Conclusion/Bibliographie)
# Durée totale : ~5 min

---

## Slide 1 — Titre

**Titre :** Peut-on caractériser les fonctions pour lesquelles la profondeur d'un réseau de neurones est strictement nécessaire ?

**Sous-titre :** Initiation à la recherche scientifique — MAM3, Polytech Nice Sophia

**Auteurs :** Zouhair Saitout · Thibaud Crotta · Romain Ben

**Visuel suggéré :** schéma simple d'un réseau shallow (1 couche, large) à gauche et d'un réseau deep (plusieurs couches, moins large) à droite

---

## Slide 2 — Pourquoi la profondeur ?

**Titre :** La profondeur : un facteur empiriquement décisif

**Contenu :**
- Les architectures modernes les plus performantes sont profondes
  - GPT-4 : ~96 couches de transformers
  - ResNet-152 : 152 couches convolutives
  - AlphaFold : blocs profonds pour la structure des protéines
- Intuition : chaque couche apprend une abstraction de plus haut niveau
- **Mais** : est-ce une nécessité théorique ou juste une heuristique qui marche ?

**Note :** mettre en évidence la tension "pratique vs théorie"

---

## Slide 3 — Le théorème d'approximation universelle

**Titre :** Un réseau peu profond suffit... en théorie

**Contenu :**

**Théorème (Cybenko, 1989) :**
> Pour toute $f \in \mathcal{C}([0,1]^d)$ et tout $\varepsilon > 0$, il existe un réseau à **1 seule couche cachée** tel que $\|f - f_N\|_\infty < \varepsilon$

- Extension : Hornik (1991) — valable pour toute activation non polynomiale

**Conséquence immédiate :** la profondeur n'est *pas nécessaire* pour l'expressivité universelle

**Mais :** ce théorème ne dit rien sur la valeur de $N$ (nombre de neurones) !

**Visuel suggéré :** équation du théorème sur fond encadré

---

## Slide 4 — Le coût caché en neurones

**Titre :** Combien de neurones faut-il vraiment ?

**Contenu :**

**Barron (1993) :** pour les fonctions à spectre de Fourier intégrable ($C_f < \infty$) :
$$\text{Erreur quadratique} \leq \frac{C_f^2}{N}$$
Borne *indépendante de la dimension* $d$ — mais valable uniquement pour cette classe.

**Pour des fonctions plus générales :** $N$ peut être **exponentiel** en $d$ ou en $1/\varepsilon$

**Exemple intuitif :** une fonction qui oscille $k$ fois nécessite $\sim k$ neurones dans un réseau shallow pour capturer chaque oscillation séparément ; un réseau profond les "compose" et en génère $2^k$ avec seulement $k$ couches.

**Visuel suggéré :** graphique comparant oscillations vs couches (zigzag à plusieurs niveaux)

---

## Slide 5 — Problématique

**Titre :** La question de recherche

**Contenu (texte centré, grande police, encadré) :**

> Peut-on **caractériser mathématiquement** la classe des fonctions pour lesquelles la profondeur est strictement nécessaire, c'est-à-dire celles dont l'approximation par un réseau peu profond requiert un nombre de neurones **exponentiellement plus grand** ?

---

*Note de transition (à dire à l'oral, pas sur la slide) :*
« Zouhair va poser le cadre formel qui permet d'étudier cette question rigoureusement. »

---

## Slide 15 — Conclusion : ce qu'on sait, ce qu'on ne sait pas

**Titre :** Bilan et questions ouvertes

**Deux colonnes :**

### Ce qui est établi
- Séparations exponentielles **prouvées** pour :
  - Fonctions zigzag (Telgarsky 2016)
  - Fonctions radiales (Eldan & Shamir 2016)
  - Fonctions à spectre sphérique de haute fréquence (Diakonikolas et al. 2022)
- Nombre de régions linéaires : exponentiel en la profondeur (Montufar et al. 2014)

### Ce qui reste ouvert
- Aucune caractérisation **nécessaire ET suffisante** générale
- Les preuves actuelles ne tiennent que si les poids sont bornés (Vardi et al. 2020)
- Extension au-delà de la sphère : ouverte

**Perspective :** la caractérisation spectrale de Diakonikolas et al. (2022) est la piste la plus prometteuse ; des liens avec la complexité booléenne ($\mathrm{NC}^1$ vs $\mathrm{AC}^0$) sont envisagés.

---

## Slide 16 — Bibliographie

**Titre :** Références principales (13 articles)

| Auteurs | Année | Conf./Journal | Contribution |
|---|---|---|---|
| Cybenko | 1989 | Math. Control | Approximation universelle (sigmoïde) |
| Hornik | 1991 | Neural Networks | Extension à act. non polynomiales |
| Barron | 1993 | IEEE Trans. IT | Borne quantitative (spectre de Fourier) |
| Pinkus | 1999 | Acta Numerica | Synthèse théorie MLP |
| Montufar et al. | 2014 | NeurIPS | Régions linéaires et profondeur |
| Eldan & Shamir | 2016 | COLT | Fonctions radiales, séparation 2/3 couches |
| Telgarsky | 2016 | COLT | Fonctions zigzag, séparation exp. |
| Raghu et al. | 2017 | ICML | Longueur de trajectoire |
| Daniely | 2017 | COLT | Séparation via polynômes de bas degré |
| Safran & Shamir | 2017 | ICML | Trade-offs profondeur-largeur |
| Yarotsky | 2017 | Neural Networks | Bornes d'erreur ReLU profond |
| Vardi et al. | 2020 | NeurIPS | Barrières formelles aux preuves |
| Diakonikolas et al. | 2022 | JMLR | Caractérisation Fourier sphérique |

**Fin de la présentation — merci pour votre attention.**
