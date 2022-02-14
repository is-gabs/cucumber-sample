clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

lint: clean flake8 check-python-import

flake8:
	@poetry run flake8 --show-source .

check-python-import:
	@poetry run isort --check-only .

fix-python-import:
	@poetry run isort .

test_unit: clean
	@poetry run pytest .

requirements: clean
	@poetry install
