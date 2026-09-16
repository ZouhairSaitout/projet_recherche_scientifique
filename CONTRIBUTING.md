# Contributing

Thank you for your interest in this project. It is a student literature review
of the introduction to scientific research course at Polytech Nice Sophia
(MAM3), written by three students, and corrections, additional references and
pull requests are welcome.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- **Report a bug** or **suggest an improvement** with the
  [issue forms](https://github.com/ZouhairSaitout/projet_recherche_scientifique/issues/new/choose).
- **Report a security vulnerability** privately, as described in the
  [security policy](SECURITY.md). Please do not open a public issue for it.
- **Open a pull request** for a fix, an additional analysis, a figure or documentation.

For a larger change, for example a new section of the report, please open an
issue first so that we can agree on the approach.

## Development setup

Requires [Tectonic](https://tectonic-typesetting.github.io/), which runs BibTeX itself.

```bash
git clone https://github.com/ZouhairSaitout/projet_recherche_scientifique.git
cd projet_recherche_scientifique/rapport
tectonic -X compile main.tex       # writes main.pdf
```

To check the Markdown files like the CI does:

```bash
npx markdownlint-cli2
lychee --offline --include-fragments .
```

## Coding guidelines

The repository provides an [`.editorconfig`](.editorconfig) file: most editors
apply its indentation and whitespace settings automatically.

- The report is written in English, limited to two pages including the
  bibliography, with `\documentclass[10pt]{article}` and the structure imposed
  by the course (context, literature review, needs). The slides and the talk
  scripts are in French.
- Every claim of the report cites a reference of `rapport/biblio.bib` with
  `\citet` or `\citep` (natbib, numeric style).
- A new reference goes to `rapport/biblio.bib` and to the bibliography table of
  the README, with a link to the publisher or to arXiv.

## Pull request process

1. Create a branch from `main` with a descriptive name, for example
   `fix/figure-labels` or `docs/results-table`.
2. Keep commits focused, with a short summary in the imperative mood
   (for example "Add the residual plot of dataset C").
3. Open a pull request against `main`, fill in the template and add a label
   (`bug`, `enhancement`, `documentation`...): labels sort the release notes.
4. The CI must pass (`report`, `docs`) and another member of the team
   reviews the pull request before it is merged. The branch is not protected
   by GitHub (a setting reserved to the owner of the repository), so this is a
   team rule rather than an enforced one.
5. Update the README when the usage or the results change, and `CHANGELOG.md`
   under "Unreleased".

## Versioning and releases

The project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (`2.0.0`): incompatible change, for example a different layout of the repository;
- **MINOR** (`1.1.0`): new section, reference or figure;
- **PATCH** (`1.0.1`): backward-compatible bug fix or correction of the report.

Releases are published from `main` with a `vX.Y.Z` tag. GitHub generates their
notes from the merged pull requests, grouped by label as configured in
[`.github/release.yml`](.github/release.yml), and the `version` field of
[`CITATION.cff`](CITATION.cff) is updated at the same time.
