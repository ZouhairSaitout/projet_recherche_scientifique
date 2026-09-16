# 🧠 Depth Separation in Neural Networks: a Literature Review

[![CI](https://github.com/ZouhairSaitout/projet_recherche_scientifique/actions/workflows/ci.yml/badge.svg)](https://github.com/ZouhairSaitout/projet_recherche_scientifique/actions/workflows/ci.yml)
[![CodeQL](https://github.com/ZouhairSaitout/projet_recherche_scientifique/actions/workflows/codeql.yml/badge.svg)](https://github.com/ZouhairSaitout/projet_recherche_scientifique/actions/workflows/codeql.yml)
[![Release](https://img.shields.io/github/v/release/ZouhairSaitout/projet_recherche_scientifique?sort=semver)](https://github.com/ZouhairSaitout/projet_recherche_scientifique/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![LaTeX](https://img.shields.io/badge/LaTeX-Tectonic-008080?logo=latex&logoColor=white)

> Can we characterise mathematically the class of functions for which the depth of a neural network is strictly necessary, that is, those whose approximation by a shallow network requires an exponentially larger number of neurons?

A single hidden layer can approximate any continuous function on a compact set (Cybenko, 1989; Hornik, 1991), yet deep networks beat wide shallow ones in practice. The paradox dissolves once the **cost** of the approximation is counted: for some targets, every shallow network must be exponentially wider than a deep one. This two-page **literature review** (`rapport/main.tex`, in English) follows that thread through thirteen papers, from the universality theorems to the only known necessary and sufficient condition, and identifies what a general characterisation still lacks.

| Context | Authors |
| --- | --- |
| Introduction to scientific research (MAM3), May 2026, Polytech Nice Sophia (Université Côte d'Azur) | Zouhair Saitout, Thibaud Crotta, Romain Ben |

## 🔍 What the Review Finds

1. **Universality says nothing about width.** Cybenko, Hornik and Pinkus guarantee existence; Barron (1993) gives the first dimension-free bound, `O(C_f² / N)`, for functions with an integrable weighted Fourier transform; Yarotsky (2017) shows that deep ReLU networks reach near-optimal rates on Sobolev balls with a depth in `log(1/ε)`.
2. **Provable separations exist.** Telgarsky's iterated triangle wave needs `2^(k/6)` neurons at constant depth but `O(k)` at depth `k`; Montufar et al. count the linear regions (exponential in depth, polynomial in width); Eldan and Shamir separate depth 2 from depth 3 with a radial function, extended to natural targets such as the Euclidean norm by Safran and Shamir.
3. **Towards a characterisation.** Daniely gives an algebraic sufficient condition, Raghu et al. a trajectory-length measure, and Diakonikolas et al. (2022) the only necessary and sufficient condition: on the sphere, a function is approximable by a polynomial-size depth-2 network if and only if its spherical Fourier spectrum concentrates on low-degree harmonics.
4. **A formal barrier.** Vardi, Yehudai and Shamir (2020) show that every known separation relies on polynomially bounded weights: with unrestricted weights a shallow network can simulate any deep one. Any future characterisation has to fix that regime, extend the spectral criterion beyond the sphere, and connect with Boolean circuit complexity.

## 📚 Bibliography

The thirteen references cited by the report, with the copies used for the review in `biblio/`.

| Reference | Link |
| --- | --- |
| Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Math. Control Signals Syst.* | [doi:10.1007/BF02551274](https://doi.org/10.1007/BF02551274) |
| Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. *Neural Networks* | [doi:10.1016/0893-6080(91)90009-T](https://doi.org/10.1016/0893-6080(91)90009-T) |
| Barron, A. R. (1993). Universal approximation bounds for superpositions of a sigmoidal function. *IEEE Trans. Inf. Theory* | [doi:10.1109/18.256500](https://doi.org/10.1109/18.256500) |
| Pinkus, A. (1999). Approximation theory of the MLP model in neural networks. *Acta Numerica* | [doi:10.1017/S0962492900002919](https://doi.org/10.1017/S0962492900002919) |
| Montufar, G., Pascanu, R., Cho, K., Bengio, Y. (2014). On the number of linear regions of deep neural networks. *NeurIPS* | [arXiv:1402.1869](https://arxiv.org/abs/1402.1869) |
| Eldan, R., Shamir, O. (2016). The power of depth for feedforward neural networks. *COLT* | [arXiv:1512.03965](https://arxiv.org/abs/1512.03965) |
| Telgarsky, M. (2016). Benefits of depth in neural networks. *COLT* | [arXiv:1602.04485](https://arxiv.org/abs/1602.04485) |
| Raghu, M., Poole, B., Kleinberg, J., Ganguli, S., Sohl-Dickstein, J. (2017). On the expressive power of deep neural networks. *ICML* | [arXiv:1606.05336](https://arxiv.org/abs/1606.05336) |
| Daniely, A. (2017). Depth separation for neural networks. *COLT* | [PMLR v65](https://proceedings.mlr.press/v65/daniely17a.html) |
| Safran, I., Shamir, O. (2017). Depth-width tradeoffs in approximating natural functions with neural networks. *ICML* | [PMLR v70](https://proceedings.mlr.press/v70/safran17a.html) |
| Yarotsky, D. (2017). Error bounds for approximations with deep ReLU networks. *Neural Networks* | [doi:10.1016/j.neunet.2017.07.002](https://doi.org/10.1016/j.neunet.2017.07.002) |
| Vardi, G., Yehudai, G., Shamir, O. (2020). Neural networks with small weights and depth-separation barriers. *NeurIPS* | [arXiv:2006.00625](https://arxiv.org/abs/2006.00625) |
| Diakonikolas, I., Kane, D. M., Kontonis, V., Zarifis, N. (2022). Depth separation beyond radial functions. *JMLR* | [jmlr.org](https://jmlr.org/papers/v23/21-1109.html) |

## 🚀 Getting Started

Requires [Tectonic](https://tectonic-typesetting.github.io/), which runs BibTeX itself.

```bash
git clone https://github.com/ZouhairSaitout/projet_recherche_scientifique.git
cd projet_recherche_scientifique/rapport
tectonic -X compile main.tex       # writes main.pdf
```

Or import `rapport/main.tex` and `rapport/biblio.bib` in Overleaf. The compiled report is in `rapport/rapport.pdf` and attached to each [release](https://github.com/ZouhairSaitout/projet_recherche_scientifique/releases).

## 📁 Repository Structure

```text
projet_recherche_scientifique/
├── rapport/
│   ├── main.tex             # the two-page report (English)
│   ├── biblio.bib           # the thirteen references (BibTeX)
│   └── rapport.pdf          # compiled report
├── slides/                  # slides of the defence (pptx) and their content per speaker (French)
├── script/                  # talk script per speaker (French)
├── biblio/                  # the papers reviewed
├── .github/                 # CI, CodeQL, Dependabot, issue forms, pull request template
├── CITATION.cff             # citation metadata
└── CHANGELOG.md             # history of the versions
```

## ✅ Quality

- **CI** (`.github/workflows/ci.yml`): the report is built with Tectonic and uploaded as an artifact, the Markdown files are checked with markdownlint and lychee.
- **CodeQL** on the workflows, **Dependabot** for the GitHub Actions.

## 👥 Authors

| Member | Part of the report | Slides |
| --- | --- | --- |
| Romain Ben | Introduction and context, conclusion, LaTeX structure and bibliography | 1 to 5, 15 and 16 |
| Zouhair Saitout | Mathematical formalism, Telgarsky and Montufar et al. | 6 to 10 |
| Thibaud Crotta | Eldan and Shamir, towards a characterisation | 11 to 14 |

## 📄 License

The report, slides and scripts are licensed under the [MIT License](LICENSE). The papers in `biblio/` belong to their authors and publishers and are kept for the review only.
