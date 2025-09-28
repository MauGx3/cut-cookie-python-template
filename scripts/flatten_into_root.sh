#!/bin/sh
# Flatten the nested template directory into the repository root.
# This script is intentionally POSIX-sh compatible so it can be executed from any shell.

set -eu
SRC="{{cookiecutter.project_name}}"
if [ ! -d "$SRC" ]; then
  echo "Source directory '$SRC' not found. Nothing to do."
  exit 1
fi
BACKUP="template-backup-$(date +%s)"
mkdir -p "$BACKUP"

# Move top-level files and dotfiles from SRC into current directory, backing up conflicts
for p in "$SRC"/* "$SRC"/.[!.]* "$SRC"/..?*; do
  [ -e "$p" ] || continue
  name=$(basename "$p")
  # Do not overwrite cookiecutter.json in the repo root
  if [ -e "$name" ] && [ "$name" != "cookiecutter.json" ]; then
    echo "Backing up existing $name to $BACKUP/"
    mv -v "$name" "$BACKUP/"
  fi
  echo "Moving $p to ."
  mv -v "$p" .
done

# Attempt to remove the now-empty source dir
rmdir -- "$SRC" 2>/dev/null || true

echo "Flatten complete. Backup of overwritten files: $BACKUP"
