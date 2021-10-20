# Formgrader Next

A jupyter extension which serves a custom LMS UI for formgrader.

## Installation

1. Install this setup directly from GitHub using `pip install`:

```bash
pip install git+ssh://git@github.com/IllumiDesk/formgradernext.git
cd formgradernext
```

2. Create and activate your virtual environment:

```bash
virtualenv -p python3 venv
source venv/bin/activate
```
3. Install NBGrader
```bash
pip install nbgrader
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader
```

4. Install and Activate formgradernext Extensions

Install and activate all extensions (assignment list, create assignment, formgrader, and validate):

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
