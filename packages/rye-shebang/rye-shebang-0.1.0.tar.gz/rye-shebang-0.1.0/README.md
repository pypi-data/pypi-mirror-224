# rye-shebang

*rye-shebang* allows you to put scripts in your path that run in a rye environment.

This solves the problem of launching `rye run script.py` from outside the script directory.

## Credits

This project is based on [*pipenv-shebang*](https://github.com/laktak/pipenv-shebang) and [*poetry-shebang*](https://github.com/ericriff/poetry-shebang).

## Usage

Put this shebang at the top of your script:

```
#!/usr/bin/env rye-shebang
```

You can also run your script with

```
rye-shebang /path/to/script
```

## Installation

```
sudo pip install rye-shebang

# or
pip install --user rye-shebang
```
