CC = clang
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 21

21: 21.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 21.py

runc: 21
	./21

clean:
	rm -f 21
