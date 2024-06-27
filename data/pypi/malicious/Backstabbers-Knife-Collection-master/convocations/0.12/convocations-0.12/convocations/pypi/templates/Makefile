SHELL := /bin/bash
VERSION := $(shell lsb_release -rs)

setup:
	if which python3.10 && [ ! -d bin ] ; then python3.10 -m venv . ; fi
	if which python3.9 && [ ! -d bin ] ; then python3.9 -m venv . ; fi
	source bin/activate \
	  && python -m pip install -U pip setuptools wheel \
	  && pip install -r requirements.txt

test: FORCE
	source bin/activate \
	  && coverage run -m pytest test \
	  && coverage report --show-missing

build:
	source bin/activate \
	  && python -B -O setup.py sdist

clean:
	source bin/activate \
	  && python -B -O setup.py clean
	rm -rf dist build
	rm -rf {{ name }}.egg-info

version:
	source bin/activate \
	  && bumpversion minor
	git push --tags

upload:
	source bin/activate \
	  && twine upload dist/*

publish: clean version build upload

FORCE:
