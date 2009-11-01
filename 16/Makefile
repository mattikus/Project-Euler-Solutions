CC = clang
CFLAGS = -Wextra -Wall -pedantic -std=c99 -ggdb
LDFLAGS = -lgmp

.PHONY: all run runpy runc clean

all: 16

16: 16.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 16.py

runc: 16
	./16

clean:
	rm -f 16 16.dSYM
