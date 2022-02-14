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

## References
---

- [`Virtual Environments`](https://dev.to/codemouse92/dead-simple-python-virtual-environments-and-pip-5b56)