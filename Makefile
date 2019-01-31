test:
	./env/bin/python -m pytest --disable-pytest-warnings tests/

up:
	docker-compose up

build:
	docker-compose build
