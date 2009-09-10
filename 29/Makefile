CC = clang
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 29

29: 29.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 29.py

runc: 29
	./29

clean:
	rm -f 29
