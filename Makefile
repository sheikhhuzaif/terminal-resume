.PHONY: install install-dev test lint format clean run

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

test:
	pytest

test-cov:
	pytest --cov=my_cli_tool --cov-report=html --cov-report=term

lint:
	flake8 src/my_cli_tool tests
	mypy src/my_cli_tool

format:
	black src/my_cli_tool tests

format-check:
	black --check src/my_cli_tool tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	python -m my_cli_tool.cli

build:
	python -m build

publish-test:
	python -m twine upload --repository testpypi dist/*

publish:
	python -m twine upload dist/*