# You can set these variables from the command line.
DIRNAME_HTML_REPORT   = coveragereport

.PHONY: help all clean test html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  setup        to install dependencies"
	@echo "  test         to execute the PyTest tests"
	@echo "  coverage     to measure, collect, and report on code coverage in Python programs"
	@echo "  html_report  to make standalone HTML files of the coverage test documentation"

all: setup test coverage html_report

########################################################################
## Install dependencies

setup:
	pip install --timeout 120 -r requirements-dev.txt 
	pip install --timeout 120 .
	@echo
	@echo "The dependencies are installed."
	@echo


########################################################################
## Tests

test: clean
	flake8 --exclude=build,docs,venv* --statistics
	pytest --flakes
	pytest --cov=pyve
	@echo
	@echo "The PyTest tests are executed."
	@echo


########################################################################
## Coverage

clean:
	rm -rf $(DIRNAME_HTML_REPORT)/
	coverage3 erase
	@echo
	@echo "The coverage data are erased."
	@echo

coverage:
	coverage3 run -m py.test tests/test_pyve.py
	@echo
	@echo "The coverage test report are finished."
	@echo

html_report:
	coverage3 html pyve.py
	@echo
	@echo "HTML report are done in $(DIRNAME_HTML_REPORT)/index.html."
	@echo

