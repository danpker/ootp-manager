FLASK_APP := src/base.py
PYTHONPATH := src
DATA_DIR := data/

run:
	DATA_DIR=$(DATA_DIR) PYTHONPATH=$(PYTHONPATH) FLASK_APP=$(FLASK_APP) flask run

lint:
	flake8 src/ scripts/
