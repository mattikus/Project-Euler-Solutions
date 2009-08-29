CC = gcc
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 4

4: 4.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 4.py

runc: 4
	./4

clean:
	rm -f 4
