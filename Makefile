VERSION=$(shell grep __version__ addressbook/__init__.py)
REQUIREMENTS="requirements/base.txt"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"


all: test


init: uninstall-addressbook
	@echo $(TAG)Installing requirements$(END)
	pip install --upgrade -r $(REQUIREMENTS)

	@echo $(TAG)Installing addressbook$(END)
	pip install --upgrade --editable .

	@echo


test: init
	@echo $(TAG)Running tests on the current Python interpreter with coverage $(END)
	py.test --cov ./addressbook --cov ./addressbook/tests --doctest-modules --verbose ./addressbook ./addressbook/tests
	@echo


clean:
	@echo $(TAG)Cleaning up$(END)
	rm -rf .tox *.egg dist build .coverage
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo


uninstall-addressbook:
	@echo $(TAG)Uninstalling addressbook$(END)
	- pip uninstall --yes addressbook &2>/dev/null

	@echo "Verifying…"
	cd .. && ! python -m addressbook --version &2>/dev/null

	@echo "Done"
	@echo


uninstall-all: uninstall-addressbook

	@echo $(TAG)Uninstalling requirements$(END)
	- pip uninstall --yes -r $(REQUIREMENTS)


test-all: uninstall-all clean init test


