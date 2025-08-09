# Quiet everything unless it errors
MAKEFLAGS += -s --no-print-directory
.SILENT:

CC      := gcc
CFLAGS  := -Wall -Wextra -pedantic -g -Ilib
LDFLAGS :=

# Parse goals ONLY if not already provided
ifndef YEAR
  YEAR := $(firstword $(MAKECMDGOALS))
endif
ifndef DAY
  DAY  := $(word 2,$(MAKECMDGOALS))
endif
DAY2 := $(shell printf "%02d" $(DAY))

SRC     := $(YEAR)/day-$(DAY2)/main.c
LIBSRC  := lib/aoclib.c
LIBHDR  := lib/aoclib.h
LIBOBJ  := build/aoclib.o
BIN     := bin/$(YEAR)/$(YEAR)-$(DAY2)

.PHONY: __dispatch help clean

__dispatch:
	@[ -n "$(YEAR)" ] && [ -n "$(DAY)" ] || { echo "Usage: make <year> <day>"; exit 2; }
	@[ -f "$(SRC)" ] || { echo "Error: missing source '$(SRC)'"; exit 1; }
	@$(MAKE) -s YEAR=$(YEAR) DAY=$(DAY) $(BIN)

# Build the library object
$(LIBOBJ): $(LIBSRC) $(LIBHDR) | build
	$(CC) $(CFLAGS) -c $< -o $@

# Link the day binary with the lib object
$(BIN): $(SRC) $(LIBOBJ) | bin/$(YEAR)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Ensure output dirs
bin/$(YEAR):
	@mkdir -p $@
build:
	@mkdir -p $@

help:
	@echo "Usage: make <year> <day>"
	@echo "Example: make 2025 1"

clean:
	@rm -rf bin build

# Glue so `make 2025 1` works
ifeq ($(words $(MAKECMDGOALS)),2)
  $(eval $(firstword $(MAKECMDGOALS)) : __dispatch)
  # Swallow the second goal quietly (no '… is up to date.')
  $(eval $(word 2,$(MAKECMDGOALS)) : ; @:)
endif
