# Formgrader Next

A jupyter extension which serves a custom LMS UI as a replacement for [nbgrader](https://github.com/jupyter/nbgrader)'s `Formgrader`.

## Requirements

- Python 3.8+
- (Recommended) Virtualenv

## Installation

1. Clone this repo:

```bash
git clone https://github.com/illumidesk/formgradernext
cd formgradernext
```

1. Create and activate your virtual environment:

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

1. Install this setup directly from GitHub using `pip install`:

```bash
pip install -e .
```

1. Install `async-nbgrader` and activate both client and server extensions:

```bash
pip install git+ssh://git@github.com/IllumiDesk/async_nbgrader.git
jupyter nbextension install --sys-prefix --py async_nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py async_nbgrader
jupyter serverextension enable --sys-prefix --py async_nbgrader
```

1. Install and activate extensions from this repo (formgradernext):

```bash
jupyter nbextension install --symlink --sys-prefix --py formgradernext --overwrite
jupyter nbextension enable --sys-prefix --py formgradernext
jupyter serverextension enable --sys-prefix --py formgradernext
```

## Contributing

For general contribution guidelines, please refer to IllumiDesk's [contributing guidelines](https://github.com/IllumiDesk/illumidesk/blob/main/CONTRIBUTING.md).

Use `pytest` to run tests:

```bash
pytest -v
```

## License

Apache 2.0
