include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 48.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 48c $<

go: 48.6
	$(GL) -o 48g $<

48.6: 48.go
	$(GC) 48.go

run: runpy runc rungo

runpy: 48.py
	python 48.py

runc: 48c
	./48c

rungo: 48g
	./48g

clean:
	rm -f 48c 48g 48.6

# :vim set ft=make:
