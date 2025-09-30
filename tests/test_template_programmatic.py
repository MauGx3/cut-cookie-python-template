import json
import os
import shutil
import tempfile

from cookiecutter.main import cookiecutter


def test_cookiecutter_programmatic_generation():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    ctx_path = os.path.join(repo_dir, '.github', 'ci', 'extra_contexts', 'empty.json')
    with open(ctx_path, 'r') as fh:
        extra = json.load(fh)

    outdir = tempfile.mkdtemp(prefix='cc-test-')
    try:
        # Generate the project programmatically using the local template directory
        cookiecutter(repo_dir, no_input=True, output_dir=outdir, directory='template', extra_context=extra)

        # There should be at least one generated project directory
        entries = [e for e in os.listdir(outdir) if os.path.isdir(os.path.join(outdir, e))]
        assert entries, f'No generated project in {outdir}'

        gen_root = os.path.join(outdir, entries[0])

        # Basic sanity checks: README.md exists
        assert os.path.exists(os.path.join(gen_root, 'README.md'))

        # The template creates a package dir named from project_slug; ensure it's present either at root or under src/
        # Default project_name is 'cut-cookie-python' so slug becomes 'cut_cookie_python'
        expected_pkg = 'cut_cookie_python'
        pkg_root = os.path.join(gen_root, expected_pkg)
        pkg_src_root = os.path.join(gen_root, 'src', expected_pkg)

        assert os.path.isdir(pkg_root) or os.path.isdir(pkg_src_root), 'Package directory not found in generated project'

    finally:
        shutil.rmtree(outdir, ignore_errors=True)
