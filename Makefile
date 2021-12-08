SHELL := /usr/bin/bash
install:
	python3 -m venv env
	./env/bin/pip install -r ./requirements.txt
	sudo apt install libimage-exiftool-perl
activate:
	source ./env/bin/activate
