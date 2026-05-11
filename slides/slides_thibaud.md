# Slides — Thibaud Crotta
# Slides 11–14 (Eldan-Shamir + Caractérisation)
# Durée estimée : ~4.5 min

---

## Slide 11 — Eldan & Shamir (2016) : fonctions radiales

**Titre :** Séparer dès la profondeur 2 vs 3

**Contenu :**

**Théorème (Eldan & Shamir 2016).** Il existe une fonction $f : \mathbb{R}^d \to \mathbb{R}$, **radiale** ($f(x) = g(\|x\|)$), telle que :

| Profondeur | Largeur nécessaire pour approcher $f$ à précision constante |
|---|---|
| **3 couches ReLU** | $\mathrm{poly}(d)$ |
| **2 couches ReLU** | $\geq \exp(\Omega(d))$ |

**Construction :** $g$ est une fonction radiale fortement oscillante en $\|x\|$.

**Idée de preuve :** analyse du spectre de Fourier en coordonnées radiales. La 3e couche permet de "reconcentrer" l'oscillation, ce que 2 couches ne peuvent faire qu'à coût exponentiel.

**Visuel suggéré :** profil radial $g(r)$ oscillant + courbe d'erreur exponentielle vs largeur

---

## Slide 12 — Daniely (2017) & Safran-Shamir (2017)

**Titre :** Séparation algébrique et trade-off largeur-profondeur

**Contenu (deux blocs) :**

### Daniely (COLT 2017)
> Un réseau ReLU à 2 couches à poids polynomialement bornés ne peut pas approcher $f$ si $f$ est loin (en $L^2$) d'un polynôme de bas degré sur $\mathbb{S}^{d-1} \times \mathbb{S}^{d-1}$.

$\Rightarrow$ **condition suffisante** de non-approximation par les réseaux peu profonds.

### Safran & Shamir (ICML 2017)
> Pour des fonctions naturelles ($f(x) = \|x\|_2$) : à précision fixée, diminuer $L$ d'un facteur multiplicatif augmente $N$ d'un facteur **exponentiel**.

$\Rightarrow$ quantification du **trade-off profondeur-largeur**.

---

## Slide 13 — Raghu et al. (2017) & Diakonikolas et al. (2022)

**Titre :** Mesure géométrique et caractérisation spectrale

**Contenu :**

### Raghu et al. (ICML 2017) — longueur de trajectoire
- Métrique : $\ell(L) = $ longueur de l'image, par le réseau, d'une courbe simple en entrée
- Résultat : $\ell(L)$ croît **exponentiellement** avec la profondeur $L$
- Interprétation : le réseau profond "plie" l'espace exponentiellement

### Diakonikolas et al. (JMLR 2022) — caractérisation Fourier sphérique
**Sur la sphère $\mathbb{S}^{d-1}$ :**
> $f$ est efficacement approchable par un réseau à 1 couche cachée de taille $\mathrm{poly}(d)$
> $\;\Longleftrightarrow\;$
> son spectre de Fourier sphérique est concentré sur des harmoniques de degré $\leq O(\mathrm{polylog}\, d)$.

$\Rightarrow$ **seule caractérisation nécessaire ET suffisante** connue, mais **uniquement sur la sphère**.

---

## Slide 14 — Vardi et al. (2020) : barrières formelles

**Titre :** Pourquoi une caractérisation générale est-elle si difficile ?

**Contenu :**

**Observation (Vardi, Yehudai, Shamir — NeurIPS 2020).**
Toutes les techniques actuelles de preuve de séparation reposent (parfois implicitement) sur l'hypothèse :

$$\|W^{(l)}\|_\infty, \|b^{(l)}\|_\infty \leq \mathrm{poly}(d)$$

**Résultat clé.** Si on autorise des poids exponentiellement grands, alors :
- Tout réseau profond peut être **simulé exactement** par un réseau peu profond
- Toutes les séparations connues (Telgarsky, Eldan-Shamir, ...) **s'effondrent**

**Conséquence.** Toute caractérisation future devra :
1. Spécifier le **régime de poids** considéré
2. S'appuyer sur des arguments qui restent valides quand cette contrainte est relâchée

---

*Note de transition (à dire à l'oral) :*
« Romain va maintenant conclure sur le bilan global et les perspectives. »
