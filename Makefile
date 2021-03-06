.PHONY: test all
.DEFAULT_GOAL := default_target

PROJECT_NAME := spreadsheet-test
PYTHON_VERSION := 3.6.6
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

setup-dev:
	pip install pip --upgrade
	pip install -U setuptools wheel==0.34.2
	pip install -r requirements-dev.txt

test:
	pytest -v --cov=sheetgo --cov-fail-under=90

test-coverage:
	pytest -v --cov=spreadsheet_test --cov-report=term-missing --cov-report=html --cov-fail-under=84

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

pycodestyle:
	echo "Running pycodestyle"
	pycodestyle

flake8:
	echo "Running flake8"
	flake8

code-convention: pycodestyle flake8

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/
	rm -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

all : setup-dev test-coverage code-convention

default_target: code-convention test

run:
	flask run