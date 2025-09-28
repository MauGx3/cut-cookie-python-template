#!/usr/bin/env sh
# Create a flattened copy of the nested template into flat-template/
# This is non-destructive and safe — review the results before replacing files in the repo root.

set -e
SRC_DIR="{{cookiecutter.project_name}}"
DST_DIR="flat-template"

if [ ! -d "$SRC_DIR" ]; then
  echo "Source folder '$SRC_DIR' not found. This script expects the template to be inside '$SRC_DIR'."
  exit 1
fi

rm -rf "$DST_DIR"
mkdir -p "$DST_DIR"

# Copy everything from the nested template into the flat dir
# We preserve file attributes and symlinks where possible
cp -a "$SRC_DIR/." "$DST_DIR/"

echo "Flattened template copied to: $DST_DIR"
echo "Review the contents and move files into the repo root if you want to publish the template at the repository root."
