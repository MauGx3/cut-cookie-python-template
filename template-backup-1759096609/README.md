# cut-cookie-python

## Introduction

This is a cookiecutter template for my personal use, so it's tailored for my taste, without any specific goal in mind.

## Acknowledgements

This project is based on [fpgmaas's](https://github.com/fpgmaas/cookiecutter-uv) template, it is extremely good and probably better than mine anyway, so you should check it out.

That project is partially based on [Audrey Feldroy\'s](https://github.com/audreyfeldroy)\'s great [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) repository.

## Usage

This repository is a Cookiecutter template. Quick examples to generate a project from it:

Local (from the repo directory):

```fish
# Generate interactively from this repository
cookiecutter /Users/mgioachini/Documents/GitHub/cut-cookie-python-template
```

Run non-interactively using defaults:

```fish
cookiecutter /Users/mgioachini/Documents/GitHub/cut-cookie-python-template --no-input
```

If you keep the template inside the nested `{{cookiecutter.project_name}}` folder (current layout), pass the `--directory` option when using the GitHub shorthand or when the template is in a subdirectory:

```fish
cookiecutter gh:owner/repo --directory="{{cookiecutter.project_name}}"
```

Recommendation: For the simplest UX (so users can run `cookiecutter gh:owner/repo` without `--directory`), consider moving the templated files up one level so `cookiecutter.json` and the template contents live in the same directory.

### Flattening the template (optional)

If you prefer to publish the repository so the template files live at the same level as `cookiecutter.json`, run the helper script which will create a `flat-template/` directory containing a copy of the template with all templated files at the top level. Review the copy before replacing files in the repo root.

```fish
./scripts/flatten_template.sh
```
