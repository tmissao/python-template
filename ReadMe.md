# Python Base Project

This is a simple python project which intends to be a a python getting start template

## Installation
---

```bash
# Installing Python
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.8 -y
python3.8 --version

# Installing Python Env and Pip
sudo apt install python3.8-venv python3-pip -y
```

## Create Virtual Environment
---

This enables a project sandbox, containing only the packages really needed, and ignoring all the Python packages installed elsewhere on your system. Conventionally, the virtual environment is called `venv`.

```bash
python3.8 -m venv venv
source venv/bin/activate
```

After that, it is not necessary to specify python version when running python commands, because all python configuration is setup in your virtual environment

In order to deactivate the python environment use the following command:

```bash
deactivate
```

## Install Dependencies
---

All python dependencies are specified at the [requirements file](./requirements.txt), and it is possible to install them using `pip`

```bash
pip install -r requirements.txt
```

## Executing
---
To execute the application, just run the following command:
```python
python -m demo
```

## Linting
---
To Execute the lint, run the below commands:
```bash
flake8 .
pylint **/*.py
```

The lint `Flake8` could be configured editing the [.flake8 file](./.flake8), and the lint `PyLint` could be configured editing the [.pylintrc file](./.pylintrc)

## Testing
---
This project utilizes the `PyTest` framework in order to run tests, this framework is configured editing the [.pytest.ini file](./pytest.ini). Also pytest-cov library is configured to create the coverage report, which could be configured through [.coveragerc file](./.coveragerc)


```bash
# execute all tests
pytest

# execute test with a specific mark #pylist.mark.<specif-mark>
pytest -m fibonacci -v
```

> To a test be analyzed it is necessary the file name be **test_\*py** or **\*_test.py**, also the function name should start with the prefix **test_\***

The coverage could be generated using this command:

```bash
# pytest --cov=<package-to-be-analyzed> --cov-report xml:coverage.xml
pytest --cov=demo --cov-report xml:coverage.xml
```


## References
---

- [`Virtual Environments`](https://dev.to/codemouse92/dead-simple-python-virtual-environments-and-pip-5b56)

- [`Project Structure`](https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6)

- [`Python Typing`](https://www.pythonsheets.com/notes/python-typing.html)

- [`VSCode Lint`](https://code.visualstudio.com/docs/python/linting)

- [`Pylint`](https://pylint.org/)

- [`Flake8`](https://flake8.pycqa.org/en/latest/)

- [`Python Linters`](https://realpython.com/python-code-quality/)

- [`PyTest`](https://www.tutorialspoint.com/pytest/index.htm)

- [`PyTest-Cov`](https://pytest-cov.readthedocs.io/en/latest/)

- [`Python Mock Class`](https://docs.python.org/3/library/unittest.mock.html#the-mock-class)

- [`PyTest-Mock Tutorial`](https://changhsinlee.com/pytest-mock/)

- [`MagicMock Tutorial`](https://aaronlelevier.github.io/python-unit-testing-with-magicmock/)

- [`MagicMock Tutorial`](https://code.tutsplus.com/tutorials/introduction-to-mocking-in-python--cms-30370)

- [`PyTest-Mock Lib`](https://pypi.org/project/pytest-mock/)

- [`SonarQube + Pytest`](https://iandrewchan.github.io/python/ci/2019/05/31/sonarqube-with-pytest.html)
