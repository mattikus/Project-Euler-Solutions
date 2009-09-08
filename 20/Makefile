CC = clang
CFLAGS = -Wall -pedantic -std=c99 -lgmp
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 20

20: 20.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 20.py

runc: 20
	./20

clean:
	rm -f 20
