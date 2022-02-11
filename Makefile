SHELL := /bin/bash

.ONESHELL:

.PHONY: install
install:
	python3 -m venv env
	./env/bin/pip install -r ./requirements.txt
	sudo apt install exiftool

run:
	. ./env/bin/activate
	flask run		

clean:
	rm -r env
