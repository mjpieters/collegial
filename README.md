# Collegial, a framework for building sane asyncio applications

## Development setup

We use [Pipenv][] to manage the developer infrastructure. Make sure it is installed and then run:

```sh
$ pipenv install --dev
$ pipenv run setup_dev
```

This installs the necessary tooling, including a pre-commit hook that enforces coding standards.

Note that this project is fully type-checked with [mypy][] in strict mode.

[Pipenv]: https://pipenv.readthedocs.io/en/latest/
[mypy]: http://www.mypy-lang.org/
