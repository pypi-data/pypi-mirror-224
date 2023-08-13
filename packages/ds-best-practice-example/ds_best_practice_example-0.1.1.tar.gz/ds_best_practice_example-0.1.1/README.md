# ds-best-practice-example


[![pypi](https://img.shields.io/pypi/v/ds-best-practice-example.svg)](https://pypi.org/project/ds-best-practice-example/)
[![python](https://img.shields.io/pypi/pyversions/ds-best-practice-example.svg)](https://pypi.org/project/ds-best-practice-example/)
[![Build Status](https://github.com/cheeyeelim/ds-best-practice-example/actions/workflows/dev.yml/badge.svg)](https://github.com/cheeyeelim/ds-best-practice-example/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/cheeyeelim/ds-best-practice-example/branch/main/graphs/badge.svg)](https://codecov.io/github/cheeyeelim/ds-best-practice-example)



Showcase best practices for structuring a simple DS-related Python package/application.

If you notice any best practice missing/incorrect, please do let me know and I will update them.

This example package will fit a linear regression on your input data. It comes with the `diabetes` data as a toy data.

Note that this example comes with many tools/components to help your development, but do enable/disable them based on your needs.

The recommend minimum tools I usually go for in most of my projects are

* [Poetry](https://python-poetry.org/) - for Python package management
* [Pre-commit](https://pre-commit.com/) - for formating and linting
* [hydra](https://hydra.cc/) - for package configurations
* [logging](https://docs.python.org/3/library/logging.html) - for logging runtime information
* [Pytest](https://docs.pytest.org/en/) - for unit testing

The additional tools are

* [Mkdocs](https://www.mkdocs.org/) - for documentation generation
* [Mkdocstrings](https://mkdocstrings.github.io/) - for automatic API generation
* [Tox](https://tox.wiki/en/) - for testing under multiple environments
* [Codecov](https://about.codecov.io/) - for code coverage report
* [GitHub Actions](https://github.com/features/actions) - for CI/CD
* [GitHub Pages](https://pages.github.com) - for documentation hosting

## Related links

* Documentation: <https://cheeyeelim.github.io/ds-best-practice-example>
* GitHub: <https://github.com/cheeyeelim/ds-best-practice-example>
* PyPI: <https://pypi.org/project/ds-best-practice-example/>
* Free software: BSD-3-Clause

## How to install this package?

The easiest way is to install it with pip.

```bash
pip install ds-best-practice-example
```

## How to run this package?

You run this package via both command line and Python.

Note that all configurations are specified via `hydra` in this [config yaml](./input/conf/config.yaml).

Please refer to the [example notebook](./notebook/ds-best-practice-example.ipynb) for more details.

### (1) Run via command line

```bash
poetry run ezml
```

### (2) Run via Python

```python
import hydra

from ezml.data import prepare_data
from ezml.model import train_model
from ezml.diagnostic import diagnose_model

# Use Hydra config with Compose API
hydra.initialize(version_base=None, config_path="../input/conf")
cfg = hydra.compose(
    config_name="config",
    overrides=["data.file_path=../input/data/diabetes.csv", "model.file_path=../output/model/linreg_diabetes.joblib"]
)

# Train linear regression with default data
X_train, X_test, y_train, y_test = prepare_data(cfg)
model = train_model(cfg, X_train, y_train)
diagnose_model(X_test, y_test, model)
```

## How to develop this package further?

1. Update codes as needed.
   1. Usually I create and test codes in Jupyter notebook (under `notebook` folder) before manually adapting over to standard Python scripts.
2. (Test locally) Test that codes are working as intended.
   1. Test locally (all in one go)
      1. `poetry run tox`
      2. Internally `tox` will run unit testing, document generation and build tests.
   2. Test locally (one by one)
      1. `poetry run pytest` for unit testing
      2. `poetry run mike deploy vtest -m "test doc build" --ignore`
      3. `poetry run mike delete vtest -m "remove doc build" --ignore`
      4. `poetry run mkdocs serve` to see docs locally
      5. `poetry build`
      6. `poetry run twine check dist/*` to test builds
    3. Test on cloud
       1. No need to do anything
       2. Follow later steps to push the codes to GitHub to trigger tests, as this repo has GitHub Workflows defined (in `.github/workflows`)
4. Run `pre-commit` by committing codes.
   1. `git add .`
   2. `git commit -m "a message"`
   3. Resolve any errors from `pre-commit` manually.
3. Bump the version number up
   1. E.g. for a patch, `poetry run bump2version patch`
4. Rerun git add and commit to commit codes.
   1. Once happy with everything, `git push` the codes to cloud repo.
5. GitHub Actions will be automatically triggered for testing and staging.
   1. Wait for GitHub Actions to complete, then check for a published package at https://test.pypi.org/project/ds-best-practice-example/
6. Once all are done, trigger `release` build by tagging a commit with `v*` version number.
   1. A documentation will be automatically generated at `https://cheeyeelim.github.io/ds-best-practice-example`
   2. The package will be built and published to `PyPI`.
7. Done!

## How to create this project from scratch?

You can create it from scratch by following the steps below.

The steps assumed `cookiecutter`, `pre-commit` and `poetry` has been installed. Otherwise follow their respective installation instructions to install them.

```bash
# Setup project folder interactively
cookiecutter https://github.com/cheeyeelim/cookiecutter-pypackage.git

# Setup pre-commit
pre-commit install

# Update pyproject.toml with required packages
# Install Python packages
poetry install -E test -E dev -E doc
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cheeyeelim/cookiecutter-pypackage](https://github.com/cheeyeelim/cookiecutter-pypackage) project template.
