SHELL := /bin/bash
VERSION := $(shell lsb_release -rs)

setup:
	if which python3.10 && [ ! -d bin ] ; then python3.10 -m venv . ; fi
	if which python3.9 && [ ! -d bin ] ; then python3.9 -m venv . ; fi
	source bin/activate \
	  && python -m pip install -U pip setuptools wheel \
	  && pip install -r requirements.txt
