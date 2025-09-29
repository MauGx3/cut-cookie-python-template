# Contributing to this Cookiecutter template

Thanks for helping improve the template. This CONTRIBUTING guide explains how to safely update template variables, hooks, and tests.

Local validation
----------------

1. Install cookiecutter in a virtualenv: `python3 -m pip install --upgrade pip cookiecutter`
2. Run the template non-interactively using one of the extra-context files in `.github/ci/extra_contexts/`:

```
python3 -m cookiecutter . --no-input --directory=template --output-dir /tmp/generated --extra-context-file .github/ci/extra_contexts/empty.json
```

3. Run the programmatic tests in `tests/` (these will be added in CI).

Editing `cookiecutter.json`
---------------------------

- When adding a new variable, include a default value and update `template/README.md` to document the variable and the prompt shown to users.
- Prefer booleans (true/false) rather than 'y'/'n' strings for binary choices to simplify Jinja conditionals and non-interactive runs.
- If you add `_extensions`, ensure the extension is available in CI or guard its use in the templates.

Hooks
-----

- Keep hooks idempotent and defensive. Always check for file existence before removing or moving files.
- Prefer to keep complex logic inside functions that are easy to unit test.

CI
--

- The project includes a cookiecutter smoke test workflow that runs the template with a small matrix of contexts. Add additional context files under `.github/ci/extra_contexts/` and include them in the workflow strategy matrix to extend coverage.

Archival backups
----------------

- If you need to restore the previous flattened content, request the `archive/template-backup-1759096609` branch (if present) or reach out to maintainers.
# Contributing to `{{cookiecutter.project_name}}`

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/issues

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

## Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

{{cookiecutter.project_name}} could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `{{cookiecutter.project_name}}` for local development.
Please note this documentation assumes you already have `uv` and `Git` installed and ready to go.

1. Fork the `{{cookiecutter.project_name}}` repo on GitHub.

2. Clone your fork locally:

```bash
cd <directory_in_which_repo_should_be_created>
git clone git@github.com:YOUR_NAME/{{cookiecutter.project_name}}.git
```

3. Now we need to install the environment. Navigate into the directory

```bash
cd {{cookiecutter.project_name}}
```

Then, install and activate the environment with:

```bash
uv sync
```

4. Install pre-commit to run linters/formatters at commit time:

```bash
uv run pre-commit install
```

5. Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

6. Don't forget to add test cases for your added functionality to the `tests` directory.

7. When you're done making changes, check that your changes pass the formatting tests.

```bash
make check
```

Now, validate that all unit tests are passing:

```bash
make test
```

9. Before raising a pull request you should also run tox.
   This will run the tests across different versions of Python:

```bash
tox
```

This requires you to have multiple versions of python installed.
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

10. Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

11. Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in `README.md`.
