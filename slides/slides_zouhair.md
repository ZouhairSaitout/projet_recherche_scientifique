# Slides — Zouhair Saitout
# Slides 6–10 (Formalisme + Résultats de séparation)
# Durée estimée : ~4.5 min

---

## Slide 6 — Formalisme : définition d'un réseau

**Titre :** Réseau de neurones feedforward

**Contenu :**

**Définition.** Un réseau feedforward de profondeur $L$ et largeurs $(n_0, n_1, \ldots, n_L)$ est la fonction
$$f_\theta(x) = h^{(L)}, \qquad h^{(0)} = x, \qquad h^{(l)} = \sigma\bigl(W^{(l)} h^{(l-1)} + b^{(l)}\bigr), \;\; 1 \leq l \leq L$$
avec $W^{(l)} \in \mathbb{R}^{n_l \times n_{l-1}}$, $b^{(l)} \in \mathbb{R}^{n_l}$.

- **Profondeur** : $L$ (nb de couches)
- **Largeur** : $\max_l n_l$
- **Activations** : sigmoïde (théorie classique), ReLU $\sigma(t) = \max(0, t)$ (résultats modernes, réseau linéaire par morceaux)

**Visuel suggéré :** schéma d'un réseau à 3 couches avec annotation $W^{(l)}, b^{(l)}, h^{(l)}$

---

## Slide 7 — Formalisme : approximation et complexité

**Titre :** Coût en neurones d'une $\varepsilon$-approximation

**Contenu :**

**Définition ($\varepsilon$-approximation).** Étant donné $f$ et $\varepsilon > 0$, on cherche $f_N$ tel que
$$\|f - f_N\|_\infty < \varepsilon \quad \text{ou} \quad \|f - f_N\|_{L^2} < \varepsilon$$

**Quantité centrale :**
$$N(\varepsilon, f, L) = \text{nombre minimal de neurones nécessaire pour approcher } f \text{ à précision } \varepsilon \text{ avec un réseau de profondeur} \leq L$$

**Séparation par profondeur :**
$$\exists f, \quad N(\varepsilon, f, L_{\text{petit}}) \;\geq\; \exp(d) \cdot N(\varepsilon, f, L_{\text{grand}})$$

Tout le travail théorique consiste à prouver de telles **bornes inférieures**.

---

## Slide 8 — Telgarsky (2016) : fonctions zigzag

**Titre :** La construction zigzag de Telgarsky

**Contenu :**

**Construction.** Dent de scie $t(x) = 2 \,|x - 1/2|$ sur $[0,1]$, puis itération :
$$t_k = \underbrace{t \circ t \circ \cdots \circ t}_{k \text{ fois}}$$
$\Rightarrow$ $t_k$ a $2^k$ morceaux linéaires.

**Théorème (Telgarsky 2016).** Soit $k \geq 1$.
- Il existe un réseau ReLU de profondeur $k$ et largeur $O(1)$ représentant $t_k$ exactement.
- Tout réseau ReLU de profondeur $\leq k/2$ qui approche $t_k$ à précision $1/2$ doit avoir
  $$\geq 2^{k/6} \text{ neurones.}$$

**Séparation exponentielle prouvée** entre profondeur $k$ et $\lfloor k/2 \rfloor$.

**Idée de preuve :** chaque couche ReLU au plus double le nombre de morceaux linéaires.

---

## Slide 9 — Illustration de la séparation de Telgarsky

**Titre :** Itérations de la dent de scie

**Visuel principal :** 4 graphes côte à côte
- $t_1$ : 2 morceaux (triangle simple)
- $t_2$ : 4 morceaux
- $t_3$ : 8 morceaux
- $t_5$ : 32 morceaux

**Commentaire écrit (bas de slide) :**
> Réseau profond : $k$ couches $\to$ $2^k$ morceaux *par composition*. Réseau peu profond : il faut $2^k$ neurones séparés pour les générer un par un.

**Note orale :** insister sur l'analogie fractale, "doublement à chaque couche"

---

## Slide 10 — Montufar et al. (2014) : régions linéaires

**Titre :** Régions linéaires et profondeur

**Contenu :**

**Théorème (Montufar et al. 2014).** Un réseau ReLU à $L$ couches de largeur $n$ en dimension $d$ peut avoir au plus
$$\Theta\!\left(\left(\tfrac{n}{d}\right)^{d(L-1)} \! n^d\right) \text{ régions linéaires.}$$

**Conséquence à nombre total de paramètres fixé ($n \cdot L = \text{const}$) :**

| Paramètre qui croît | Croissance du nb de régions |
|---|---|
| Profondeur $L$ | **Exponentielle** |
| Largeur $n$ | Polynomiale |

$\Rightarrow$ la profondeur est **exponentiellement plus efficace** que la largeur pour générer de la complexité géométrique.

---

*Note de transition (à dire à l'oral) :*
« Thibaud va maintenant présenter les séparations encore plus fortes (2 vs 3 couches) et les tentatives de caractérisation générale. »
