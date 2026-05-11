# Script oral — Zouhair Saitout
# Slides : 6, 7, 8, 9, 10
# Durée estimée : ~4.5 min

---

## [Slide 6 — Définition formelle d'un réseau] (~1 min)

« Merci Romain. Avant de présenter les résultats théoriques, posons un cadre précis.

Un réseau de neurones feedforward de profondeur L est une fonction qui transforme une entrée x
en une sortie par compositions successives. Chaque couche l calcule h^(l) = sigma(W^(l) h^(l-1)
+ b^(l)), où sigma est la fonction d'activation, W^(l) une matrice de poids, et b^(l) un biais.

Deux quantités importantes : la profondeur L, c'est-à-dire le nombre de couches, et la largeur,
c'est-à-dire la taille maximale des couches intermédiaires. Le nombre total de neurones est
proportionnel au produit largeur fois profondeur.

Pour les fonctions d'activation, deux choix dominent dans la théorie : la sigmoïde, utilisée
dans les résultats classiques de Cybenko, et le ReLU défini par sigma(t) = max(0, t), qui est
au cœur de tous les résultats modernes de séparation par profondeur car il rend le réseau
linéaire par morceaux. »

---

## [Slide 7 — Approximation et complexité] (~1 min)

« Une fois ce cadre fixé, on peut définir précisément ce que veut dire approcher une fonction.
Étant donné une cible f et une précision epsilon, on cherche un réseau f_N tel que la distance
entre f et f_N, en norme sup ou en norme L^2, soit inférieure à epsilon.

La quantité centrale de toute la théorie est N(epsilon, f, L) : le nombre minimal de neurones
nécessaire pour approcher f à précision epsilon avec un réseau de profondeur au plus L.

La séparation par profondeur, formellement, c'est l'existence de fonctions pour lesquelles
N(epsilon, f, L_petit) est exponentiellement plus grand que N(epsilon, f, L_grand). C'est ce
type de bornes inférieures qu'il faut prouver. »

---

## [Slide 8 — Telgarsky : fonctions zigzag] (~1 min 30)

« Le premier résultat marquant est dû à Telgarsky, en 2016. Sa construction est élégante : on
part de la fonction dent de scie t(x) = 2 fois la valeur absolue de x moins un demi, sur
l'intervalle [0,1]. Puis on itère : t_k est la composition de t avec elle-même k fois.

Géométriquement, t_k oscille 2^k fois sur [0,1]. Et voici le théorème : un réseau ReLU de
profondeur k peut représenter t_k exactement avec seulement O(k) neurones. Mais, et c'est le
point fort, tout réseau ReLU de profondeur inférieure ou égale à k/2 qui approche t_k à
précision constante, disons 1/2, doit avoir au moins 2 puissance k/6 neurones.

C'est une séparation exponentielle nette : la profondeur k apporte un gain exponentiel par
rapport à la profondeur k/2. La preuve repose sur le fait que chaque couche ReLU peut au plus
doubler le nombre de morceaux linéaires de la fonction représentée. »

---

## [Slide 9 — Illustration géométrique] (~30 s)

« Voici visuellement les premières itérations. t_1 a deux morceaux linéaires, t_2 en a quatre,
t_3 en a huit. Pour approcher t_10, qui a 1024 oscillations, un réseau peu profond doit
"gérer" chaque oscillation séparément. Un réseau profond, lui, compose les doublements à
chaque couche, et obtient les 1024 morceaux avec dix couches seulement. C'est l'intuition
fondamentale de la séparation par profondeur. »

---

## [Slide 10 — Montufar : régions linéaires] (~30 s)

« Cette intuition est confirmée par Montufar et ses coauteurs. Pour un réseau ReLU à L couches
de largeur n en dimension d, ils prouvent que le nombre maximal de régions linéaires est de
l'ordre de (n/d)^(d(L-1)) fois n^d.

À nombre total de paramètres fixé, ce nombre croît exponentiellement avec L mais seulement
polynomialement avec la largeur n. Autrement dit, la profondeur est exponentiellement plus
efficace que la largeur pour générer de la complexité géométrique.

Thibaud va maintenant présenter d'autres résultats de séparation et les tentatives de
caractérisation générale. »
