#!/bin/sh
# Move templated artifacts into a new template/ folder, restore repo root files from backup
set -eu
ROOT="$(pwd)"
BACKUP_DIR="${ROOT}/template-backup-1759096609"
TEMPLATE_DIR="${ROOT}/template"

mkdir -p "$TEMPLATE_DIR"

# Files/dirs that belong to template (detect heuristically)
CANDIDATES="README.md Makefile mkdocs.yml pyproject.toml LICENSE LICENSE_APACHE LICENSE_BSD LICENSE_GPL LICENSE_ISC LICENSE_MIT docs tests {{cookiecutter.project_slug}}"

for name in $CANDIDATES; do
  if [ -e "$ROOT/$name" ]; then
    echo "Moving $name -> template/"
    mv "$ROOT/$name" "$TEMPLATE_DIR/"
  else
    echo "Skipping $name (not present)"
  fi
done

# Move cookiecutter.json into template/ if its
