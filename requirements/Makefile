.PHONY: all help requirements requirements.txt

REQS=.reqs
REQUIRE=../requirements.txt
REQFILE=base.txt
MINVERS=MINVERS.txt

all: $(MINVERS) $(REQUIRE)

help:
	@echo "Help"
	@echo "----"
	@echo
	@echo "  requirements - (re)generate pinned and minimum requirements"
	@echo "  test - test and check Python code for requirements"

# Perform forced build using -W for the (.PHONY) requirements target
requirements:
	$(MAKE) -W $(REQFILE) $(MINVERS) $(REQUIRE)

$(notdir $(REQUIRE)): $(REQUIRE)
requirements/%: %
	@echo "make: '$@' is up to date."

$(REQUIRE): $(REQFILE) freeze
	./freeze $@ $(wildcard py*.txt) $<

$(MINVERS): [a-z]*.txt
	./minvers $@ $(filter %.txt, $(filter-out py%.txt, $^))


.PHONY: test
.INTERMEDIATE: freeze.py

SHELL=/bin/bash

test: freeze.pyc
	-pep8 freeze
	-pylint -r n -f parseable -i y -d I0011 freeze
	python -Wd -Werror -m doctest freeze
	python -Wd freeze $(wildcard py*.txt) $(REQFILE)
	! diff $(REQFILE) $(REQS)/$(REQFILE) | grep -v			 \
	   -f <(echo '^---$$'; echo '^[0-9]*c[0-9]*$$'; echo '^. \#*-r'; \
	        sed 's/<.*//' py*.txt)

%.pyc: %.py
	python -tt -m $*

freez%.py: freez%
	ln -s $< $@
