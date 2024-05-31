SHELL := /bin/bash
build:
	source venv/bin/activate \
	  && convoke build
setup:
	if [[ ! -e ./venv/bin/python ]] ; then python3.9 -m venv venv ; fi \
	  && source venv/bin/activate \
	  && pip install -U setuptools wheel \
	  && pip install awscli botocore boto3 \
	  && pip install -r requirements.txt
publish:
	source venv/bin/activate \
	  && convoke publish

