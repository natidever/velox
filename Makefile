.PHONY: build run test

build:
	docker-compose build --no-cache

run:
	docker-compose up

test:
	docker-compose run --rm web pytest

install-dev:
	pip install -e .