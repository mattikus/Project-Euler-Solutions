CC = clang
CFLAGS = -Wall -pedantic -std=c99
LDFLAGS = 

.PHONY: all run runpy runc clean

all: 9

9: 9.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

run: runpy runc

runpy:
	python 9.py

runc: 9
	./9

clean:
	rm -f 9
