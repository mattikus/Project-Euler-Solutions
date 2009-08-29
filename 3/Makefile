CC = gcc
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 3

3: 3.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 3.py

runc: 3
	./3

clean:
	rm -f 3
