## Summary

<!-- What does this pull request change, and why? Link the related issue, for example "Closes #12". -->

## Type of change

- [ ] Bug fix
- [ ] New analysis, figure or section of the report
- [ ] Documentation
- [ ] CI, dependencies or tooling

## Checklist

- [ ] `tectonic -X compile main.tex` (from `rapport/`) builds the report and it stays within two pages
- [ ] A new reference is added to `rapport/biblio.bib` and to the bibliography table of the README
- [ ] `npx markdownlint-cli2` and `lychee --offline --include-fragments .` pass (if Markdown files changed)
- [ ] `CHANGELOG.md` is updated under "Unreleased"
