export MOZ_HEADLESS = 1
export GECKODRIVER_LOG = $(shell pwd)/results/geckodriver.log

MINIMUM_COVERAGE = 50
FLAKE8_CHECK = flake8 .
MYPY_CHECK = mypy .
TESTS = pytest -vvv --cov --cov-fail-under=$(MINIMUM_COVERAGE) --html results/report.html

check: install_poetry lint typecheck test

install_poetry:
	curl -sSL https://install.python-poetry.org | python3 -

install_dependencies:
	poetry install

test: install_dependencies
	poetry run $(TESTS)

lint: install_dependencies
	poetry run $(FLAKE8_CHECK)

typecheck: install_dependencies
	poetry run $(MYPY_CHECK)
