# You can set these variables from the command line.
TITLE_HTML_REPORT     = "Coverage report from pyve package"
DIRNAME_HTML_REPORT   = coveragereport

.PHONY: help all clean test html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  setup      to install dependencies"
	@echo "  test       to run the PyTest tests"
	@echo "  coverage   to make standalone HTML files of the coverage test documentation"

all: setup test coverage 

########################################################################
## Install dependencies

setup: 
	pip install --timeout 120 -r requirements-dev.txt 
	pip install --timeout 120 .


########################################################################
## Tests

test: clean
	py.test --flakes
	pytest tests/test_pyve.py
	@echo
	@echo "The PyTests are done."
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
	coverage3 html --title=$(TITLE_HTML_REPORT) pyve.py
	@echo
	@echo "HTML report are finished in $(DIRNAME_HTML_REPORT)/html/index.html."
	@echo

