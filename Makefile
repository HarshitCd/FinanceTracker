PYTHON := python3
PIP := pip3

VENV_NAME := venv
VENV_BIN := $(VENV_NAME)/bin

venv:
	$(PYTHON) -m venv $(VENV_NAME)

install:
	$(VENV_BIN)/$(PIP) install -r requirements.txt 

setup:
	make venv
	make install

run:
	$(VENV_BIN)/$(PYTHON) src/main.py

clean:
	rm -rf $(VENV_NAME)