# Script oral — Thibaud Crotta
# Slides : 11, 12, 13, 14
# Durée estimée : ~4.5 min

---

## [Slide 11 — Eldan & Shamir : fonctions radiales] (~1 min 30)

« Merci Zouhair. Telgarsky donne une séparation entre profondeur k et k/2, mais on peut aller
plus loin et séparer dès la profondeur 2 et la profondeur 3. C'est le résultat d'Eldan et
Shamir en 2016, qui est probablement le plus surprenant de toute la littérature.

Ils construisent explicitement une fonction f de R^d dans R, avec les propriétés suivantes :
elle est radiale, c'est-à-dire qu'elle ne dépend que de la norme de x, et fortement oscillante
en cette norme. Et voici le théorème : il existe un réseau ReLU à 3 couches, de taille
polynomiale en d, qui approche f à précision constante. Mais tout réseau ReLU à 2 couches qui
réalise la même approximation doit avoir au moins exp(d) neurones.

C'est une séparation exponentielle entre 2 et 3 couches, en dimension d. La preuve utilise une
analyse fine du spectre de Fourier de f en coordonnées radiales : la troisième couche permet
de "rapprocher" l'oscillation, ce que deux couches sont incapables de faire sans payer
exponentiellement cher. »

---

## [Slide 12 — Daniely & Safran-Shamir] (~1 min)

« Daniely en 2017 reformule la séparation par profondeur dans un langage plus algébrique. Son
résultat dit qu'un réseau ReLU à 2 couches, à poids polynomialement bornés, ne peut pas
approcher une fonction qui est loin d'être un polynôme de bas degré sur le produit de sphères
S^(d-1) fois S^(d-1). Cela donne une condition suffisante de non-approximation par les
réseaux peu profonds.

Safran et Shamir, la même année, complètent ce tableau en quantifiant le trade-off
profondeur-largeur sur des fonctions naturelles, comme la norme euclidienne f(x) = ||x||_2.
Ils montrent qu'à précision fixée, diminuer la profondeur d'un facteur multiplicatif augmente
la largeur requise d'un facteur exponentiel. »

---

## [Slide 13 — Raghu & Diakonikolas] (~1 min)

« Une autre façon de mesurer l'expressivité est due à Raghu et ses coauteurs en 2017. Ils
mesurent la longueur de l'image, par le réseau, d'une courbe simple en entrée, par exemple un
segment. Cette longueur croît exponentiellement avec la profondeur pour les réseaux profonds,
ce qui formalise géométriquement leur "capacité à plier l'espace".

Le résultat le plus complet à ce jour est dû à Diakonikolas et al., en 2022. Sur la sphère
unité S^(d-1), ils établissent une caractérisation précise : une fonction est efficacement
approchable par un réseau à une couche cachée de taille polynomiale si et seulement si son
spectre de Fourier sphérique est concentré sur des harmoniques de degré au plus
polylogarithmique en d. C'est, à notre connaissance, la seule condition nécessaire et
suffisante connue, mais elle est restreinte à la sphère. »

---

## [Slide 14 — Vardi : barrières formelles] (~30 s)

« Pour terminer, un résultat important de Vardi, Yehudai et Shamir en 2020 explique pourquoi
une caractérisation générale est si difficile. Ils prouvent que toutes les techniques actuelles
de preuve de séparation reposent, parfois implicitement, sur l'hypothèse que les poids du
réseau peu profond sont polynomialement bornés. Si on autorise des poids exponentiellement
grands, un réseau peu profond peut simuler exactement un réseau profond, et toutes les
séparations connues s'effondrent.

C'est ce qu'on appelle une barrière formelle : toute future caractérisation devra spécifier
le régime de poids dans lequel elle est valable. Je passe maintenant la parole à Romain pour
la conclusion. »
