FLASK_APP := src/base.py
PYTHONPATH := src
CONFIG := config.yaml

run:
	CONFIG=$(CONFIG) PYTHONPATH=$(PYTHONPATH) FLASK_APP=$(FLASK_APP) flask run

lint:
	flake8 src/ scripts/
