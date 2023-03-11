# django-fakemessages - Generate fake language files for your [Django Project](https://djangoproject.com/)

[![CI tests](https://github.com/pfouque/django-fakemessages/actions/workflows/test.yml/badge.svg)](https://github.com/pfouque/django-fakemessages/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/pfouque/django-fakemessages/branch/master/graph/badge.svg?token=GWGDR6AR6D)](https://codecov.io/github/pfouque/django-fakemessages)
[![Documentation](https://img.shields.io/static/v1?label=Docs&message=READ&color=informational&style=plastic)](https://github.com/pfouque/django-fakemessages#settings)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=informational&style=plastic)](https://github.com/pfouque/django-fakemessages/LICENSE)


## Introduction

Looking for missing translations in your Django project? Let's censor what is done and see what remains!

## Resources

-   Package on PyPI: [https://pypi.org/project/django-fakemessages/](https://pypi.org/project/django-fakemessages/)
-   Project on Github: [https://github.com/pfouque/django-fakemessages](https://github.com/pfouque/django-fakemessages)

## Requirements

-   Django >=3.2
-   Python >=3.8
-   Translate-toolkit >=3.8.5

## How to

1. Install
    ```
    $ pip install "django-fakemessages"
    ```

2. Register fakemessage in your list of Django applications:
    ```
    INSTALLED_APPS = [
        # ...
        "fakemessages",
        # ...
    ]
    ```

3. Update your settings:
    ```
    if DEBUG:
        """Add our fake language to Django"""
        from django.conf.locale import LANG_INFO

        FAKE_LANGUAGE_CODE = "kl"

        LANG_INFO[FAKE_LANGUAGE_CODE] = {
            "bidi": False,
            "code": FAKE_LANGUAGE_CODE,
            "name": "▮▮▮▮▮▮▮▮",
            "name_local": "🖖 ▮▮▮▮▮▮▮",
        }
        LANGUAGES.append((FAKE_LANGUAGE_CODE, "🖖 ▮▮▮▮▮▮▮"))
    ```

4. 🎉 Voila!


## Contribute

### Principles

-   Simple for developers to get up-and-running
-   Consistent style (`black`, `ruff`)
-   Future-proof (`pyupgrade`)
-   Full type hinting (`mypy`)

### Coding style

We use [pre-commit](https://pre-commit.com/) to run code quality tools.
[Install pre-commit](https://pre-commit.com/#install) however you like (e.g.
`pip install pre-commit` with your system python) then set up pre-commit to run every time you
commit with:

```bash
> pre-commit install
```

You can then run all tools:

```bash
> pre-commit run --all-files
```

It includes the following:

-   `poetry` for dependency management
-   `Ruff`, `black` and `pyupgrade` linting
-   `mypy` for type checking
-   `Github Actions` for builds and CI

There are default config files for the linting and mypy.

### Tests

#### Tests package

The package tests themselves are _outside_ of the main library code, in a package that is itself a
Django app (it contains `models`, `settings`, and any other artifacts required to run the tests
(e.g. `urls`).) Where appropriate, this test app may be runnable as a Django project - so that
developers can spin up the test app and see what admin screens look like, test migrations, etc.

#### Running tests

The tests themselves use `pytest` as the test runner. If you have installed the `poetry` evironment,
you can run them thus:

```
$ poetry run pytest
```

or

```
$ poetry shell
(django-fakemessages-py3.10) $ pytest
```

#### CI

- `.github/workflows/lint.yml`: Defines and ensure coding rules on Github.

- `.github/workflows/test.yml`: Runs tests on all compatible combinations of Django (3.2+) & Python (3.8+) in a Github matrix.

- `.github/workflows/coverage.yml`: Calculates the coverage on an up to date version.
