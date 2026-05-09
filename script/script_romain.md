# Script oral — Romain Ben
# Slides : 1, 2, 3, 4, 5, 15, 16
# Durée estimée : 5 min (intro ~3 min + conclusion ~2 min)

---

## [Slide 1 — Titre] (~10 secondes)

« Bonjour à tous. Notre groupe s'est intéressé à une question de théorie de l'approximation
appliquée aux réseaux de neurones : peut-on caractériser mathématiquement les fonctions pour
lesquelles la profondeur est réellement irremplaçable ? Je vais d'abord vous expliquer d'où
vient cette question. »

---

## [Slide 2 — Pourquoi la profondeur ?] (~50 secondes)

« Si vous avez utilisé ChatGPT, regardé une photo reconnue par votre téléphone, ou entendu
parler d'AlphaFold, vous savez que les systèmes les plus performants aujourd'hui sont tous
des réseaux de neurones très profonds : des dizaines, voire des centaines de couches.

L'intuition, c'est que chaque couche apprend une représentation de plus en plus abstraite :
les premières couches détectent des bords, les suivantes des formes, les dernières des concepts.

Mais est-ce que la profondeur est une nécessité théorique, ou juste une heuristique qui marche
empiriquement et dont on pourrait se passer ? C'est exactement la question que ce travail
cherche à éclairer. »

---

## [Slide 3 — Théorème d'approximation universelle] (~55 secondes)

« La première réponse théorique à cette question semble rassurante pour les réseaux peu
profonds. En 1989, Cybenko démontre un résultat surprenant : un réseau à une seule couche
cachée peut approcher n'importe quelle fonction continue sur un compact, avec n'importe
quelle précision.

Ce théorème, étendu par Hornik en 1991 à des fonctions d'activation plus générales, dit en
substance que la profondeur n'est pas nécessaire pour l'expressivité.

Si on s'arrêtait là, on conclurait que les réseaux profonds ne sont qu'une mode, et qu'un
réseau large mais plat suffit toujours. Mais ce théorème cache un point crucial qu'il omet
complètement. »

---

## [Slide 4 — Le coût caché en neurones] (~1 min)

« Ce point crucial, c'est le nombre N de neurones. Le théorème dit qu'il en existe un N qui
convient, mais il ne dit pas quelle est sa valeur.

Barron, en 1993, a montré une borne quantitative intéressante : pour les fonctions dont la
transformée de Fourier est intégrable, N neurones donnent une erreur de l'ordre de C_f au
carré sur N — une borne indépendante de la dimension. C'est bien, mais cette classe de
fonctions est assez restrictive.

Pour des fonctions plus générales, et en particulier pour les fonctions très oscillantes, le
nombre de neurones requis par un réseau peu profond peut être exponentiel.

L'intuition géométrique, c'est ça : imaginez une fonction qui oscille mille fois sur [0,1].
Un réseau à une couche doit avoir autant de neurones qu'il y a d'oscillations pour les
représenter séparément. Un réseau profond, lui, peut composer les oscillations à chaque
couche et en générer exponentiellement plus — deux fois plus à chaque couche, comme une
fractale. »

---

## [Slide 5 — Problématique] (~25 secondes)

« Ce phénomène s'appelle la séparation par profondeur. On sait qu'il existe pour certaines
familles de fonctions. La question plus ambitieuse est : peut-on caractériser mathématiquement
toutes les fonctions pour lesquelles ce phénomène se produit ?

Zouhair va maintenant formaliser ce cadre, avant que Thibaud présente les tentatives de
réponse les plus récentes. »

---

[Zouhair présente ses slides 6–10 (~4.5 min)]
[Thibaud présente ses slides 11–14 (~4.5 min)]

---

## [Slide 15 — Conclusion] (~1 min 20 secondes)

« Pour conclure, les travaux que nous avons présentés montrent deux choses.

D'un côté, la séparation par profondeur est un phénomène réel et rigoureusement prouvé pour
plusieurs familles spécifiques. Telgarsky avec ses fonctions zigzag, Eldan et Shamir avec
leurs fonctions radiales, Diakonikolas et al. avec la caractérisation spectrale sur la
sphère : tous ces travaux confirment que la profondeur fait une différence exponentielle pour
certaines fonctions.

De l'autre côté, une caractérisation générale reste hors de portée. Vardi et ses coauteurs
ont identifié une barrière formelle : toutes les preuves actuelles supposent des poids bornés
polynomialement. Si on lève cette contrainte, les séparations connues disparaissent. Ca montre
que le problème est structurellement plus difficile qu'il n'y paraît.

La piste la plus prometteuse aujourd'hui, c'est la caractérisation spectrale de Diakonikolas
et al., qui donne une condition nécessaire et suffisante sur la sphère. L'étendre à des
domaines plus généraux, et comprendre le lien avec la théorie de la complexité, sont les
prochaines étapes naturelles.

La profondeur des réseaux de neurones n'est donc pas qu'un choix d'ingénierie : c'est un
paramètre fondamental dont la théorie reste un problème ouvert. »

---

## [Slide 16 — Bibliographie] (~15 secondes)

« Nos 13 références principales sont listées ici. Les PDFs sont disponibles dans le dossier
biblio du repo GitHub. Merci pour votre attention, nous sommes disponibles pour des
questions. »
