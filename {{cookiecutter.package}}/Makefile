PROJECT_LOGO = {{cookiecutter.logo}}

all: update build install test requirements notebook

install-poetry :
	pip install --upgrade pip
	pip install --upgrade poetry

POETRY := $(shell poetry -V 2>/dev/null)
check-poetry :
ifndef POETRY
	make install-poetry
else
	$(info ${PROJECT_LOGO} is using ${POETRY})
endif

update: check-poetry
	poetry update

requirements: check-poetry
	poetry export --format requirements.txt --output requirements.pip --without-hashes --dev

build : check-poetry
	poetry build --format sdist

PRE-COMMIT := $(shell pre-commit -V 2>/dev/null)
check-pre-commit :
ifndef PRE-COMMIT
	poetry add --dev pre-commit
	pre-commit install
else
	$(info ${PROJECT_LOGO} is using ${PRE-COMMIT})
endif

install : check-poetry check-pre-commit
	poetry install

PYTEST := $(shell pytest -V 2>/dev/null 2>&1)
check-pytest :
ifndef PYTEST
	poetry add --dev pytest
else
	$(info ${PROJECT_LOGO} is using ${PYTEST})
endif

test : check-poetry check-pytest
	poetry run pytest src/test/python

JUPYTER := $(shell jupyter --version 2>/dev/null)
check-jupyter :
ifndef JUPYTER
	poetry add --dev jupyter
else
	$(info ${PROJECT_LOGO} is using ${JUPYTER})
endif

notebook : check-jupyter
	jupyter notebook --autoreload
