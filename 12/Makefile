CC = clang
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS =

.PHONY: all run runpy runc clean

all: 12

12: 12.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 12.py

runc: 12
	./12

clean:
	rm -f 12
