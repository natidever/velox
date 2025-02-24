.PHONY: build run test

build:
	docker-compose build --no-cache

run_dev:
	@echo "Running Configuration Commands"
	export DOCKER_GID=$(id -g)
	export DOCKER_UID=$(id -u)
	@echo "Running Configuration Commands"
	docker-compose up app_dev

run_prod:
	docker-compose up app_prod


down:
	docker-compose down

test:
	docker-compose run --rm web pytest

install-dev:
	pip install -e .



   # export DOCKER_GID=$(id -g)
   # export DOCKER_UID=$(id -u)