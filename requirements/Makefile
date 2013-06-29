.PHONY: all help requirements requirements.txt

all: requirements

help:
	@echo "Help"
	@echo "----"
	@echo
	@echo "  requirements - (re)generate pinned and minimum requirements"

REQS=.reqs
REQUIRE=../requirements.txt
REQFILE=base.txt
MINVERS=MINVERS.txt

# Perform forced build using -W for the (.PHONY) requirements target
requirements:
	$(MAKE) -W $(REQFILE) $(MINVERS) $(REQUIRE)

$(notdir $(REQUIRE)): $(REQUIRE)
requirements/%: %
	@echo "make: '$@' is up to date."

$(REQUIRE): $(REQFILE) freeze
	./freeze $@ $<

$(MINVERS): [a-z]*.txt minvers
	./minvers $@ $(filter %.txt, $(filter-out py%.txt, $^))
