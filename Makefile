SHELL := /bin/bash

.ONESHELL:

.PHONY: install
install:
	python3 -m venv env
	./env/bin/pip install -r ./requirements.txt
	apt install exiftool

run:
	. ./env/bin/activate
	flask run		

clean:
	rm -r env
