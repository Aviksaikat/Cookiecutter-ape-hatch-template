# Cookiecutter-ape-hatch-template
Simple Cookiecutter template for [`Ape`](https://github.com/ApeWorX/ape) (ApeWorx) with `Hatch`, `ruff`, `mypy`.



|         |                                    |
|---------|------------------------------------|
| Details | [![License - MIT][MIT-image]][MIT-link] [![GitHub Sponsors][sponsor-image]][sponsor-link] |
| Features | [![Hatch project][hatch-image]][hatch-link] [![linting - Ruff][ruff-image]][ruff-link] [![types - mypy][mypy-image]][mypy-link] [![test - pytest][pytest-image]][pytest-link] [![linting - precommit][precommit-image]][precommit-link] [![docs - mkdocs][mkdocs-image]][mkdocs-link]



## ✨ Features

* [X] Lightweight [`Ape`](https://github.com/ApeWorX/ape) starter
* [X] [`Hatch`](https://hatch.pypa.io/latest/install/) package management
* [X] Linting and formatting with [`ruff`](https://github.com/charliermarsh/ruff) which replaces [isort], [flake8], [black], etc.
* [X] Type checking with [`mypy`](https://github.com/python/mypy)
* [X] Unit tests with [`pytest`](https://github.com/pytest-dev/pytest) with optional asyncio setup.
* [X] Automate and standardize testing with [Hatch-env-matrices]
* [X] Documentation with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and docstring reference support with [mkdocstrings](https://mkdocstrings.github.io/).
* [X] [pyproject.toml]: all package, build and tool configuration in one file,
* [X] [pre-commit]: pre-commit git hooks that make your life easier,
* [X] [Markdown]: instead of reStructuredText, Markdown is used consistently for all text files


## Demo
![](./media/demo.gif)

## 💫 Quickstart

Generate the project:

This project will use [`pipx`](https://github.com/pypa/pipx) to install `hatch` in an isolated enviroment. Make sure you have `pipx` installed before running the following command.

```bash
cookiecutter https://github.com/Aviksaikat/Cookiecutter-ape-hatch-template
```

The generator will automatically call `hatch env create` at the end.


### With cruft

[cruft](https://github.com/cruft/cruft) is a layer above Cookiecutter allowing you to update your project from the template after it has been generated.

```bash
cruft create https://github.com/Aviksaikat/Cookiecutter-ape-hatch-template
```

## License

This project is licensed under the terms of the [MIT](https://github.com/Aviksaikat/Cookiecutter-ape-hatch-template/blob/main/LICENSE) license.



[cookiecutter]: https://cookiecutter.readthedocs.io/
[Hatch-env-matrices]: https://hatch.pypa.io/dev/config/environment/advanced/#matrix
[cookiecutter-pypackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[pre-commit]: https://pre-commit.com/
[mkdocs]: https://www.mkdocs.org/
[Markdown]: https://www.markdownguide.org/
[flake8]: https://pypi.org/project/flake8/
[isort]: https://pycqa.github.io/isort/
[pytest]: https://docs.pytest.org/
[mypy]: https://mypy-lang.org/
[black]: https://black.readthedocs.io/
[ruff]: https://beta.ruff.rs/
[pyproject.toml]: https://hatch.pypa.io/latest/config/metadata/
[`README.md`]: https://github.com/aviksaikat/the-hatchlor-demo

[Tests-image]: https://github.com/aviksaikat/the-hatchlor/actions/workflows/run-tests.yml/badge.svg?branch=main
[Tests-link]: https://github.com/aviksaikat/the-hatchlor/actions/workflows/run-tests.yml
[hatch-image]: https://img.shields.io/badge/%F0%9F%A5%9A-hatch-4051b5.svg
[hatch-link]: https://github.com/pypa/hatch
[ruff-image]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff-link]: https://github.com/charliermarsh/ruff
[mypy-image]: https://img.shields.io/badge/Types-mypy-blue.svg
[mypy-link]: https://mypy-lang.org/
[pytest-image]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white
[pytest-link]:  https://docs.pytest.org/
[mkdocs-image]: https://img.shields.io/badge/Docs-mkdocs-blue.svg
[mkdocs-link]: https://www.mkdocs.org/
[precommit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[precommit-link]:  https://pre-commit.com/
[MIT-image]: https://img.shields.io/badge/License-MIT-9400d3.svg
[MIT-link]: LICENSE
[sponsor-image]: https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4
[sponsor-link]: https://github.com/sponsors/aviksaikat