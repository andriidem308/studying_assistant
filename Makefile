MANAGE = python3 manage.py
PROJECT_DIR = $(shell pwd)

run:
	$(MANAGE) runserver

make-migration:
	$(MANAGE)  makemigrations

migrate:
	$(MANAGE) migrate

lint:
	flake8 .