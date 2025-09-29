#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(path):
        os.remove(path)


def remove_dir(filepath: str) -> None:
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(path):
        shutil.rmtree(path)


def move_file(filepath: str, target: str) -> None:
    src = os.path.join(PROJECT_DIRECTORY, filepath)
    dst = os.path.join(PROJECT_DIRECTORY, target)
    if os.path.exists(src):
        # Ensure target directory exists
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        os.rename(src, dst)


def move_dir(src: str, target: str) -> None:
    src_path = os.path.join(PROJECT_DIRECTORY, src)
    dst_path = os.path.join(PROJECT_DIRECTORY, target)
    if os.path.exists(src_path):
        # Ensure target directory parent exists
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.move(src_path, dst_path)


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to_pypi}}" == "n":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "ISC license":
        move_file("LICENSE_ISC", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "Apache Software License 2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.layout}}" == "src":
        if os.path.isdir("src"):
            remove_dir("src")
        move_dir("{{cookiecutter.project_slug}}", os.path.join("src", "{{cookiecutter.project_slug}}"))
