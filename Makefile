lint:
	flake8

test:
	poetry run pytest

fix:
	python3 -m black ./
