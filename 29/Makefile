include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 29.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 29c $<

go: 29.6
	$(GL) -o 29g $<

29.6: 29.go
	$(GC) 29.go

run: runpy runc rungo

runpy: 29.py
	python 29.py

runc: 29c
	./29c

rungo: 29g
	./29g

clean:
	rm -f 29c 29g 29.6

# :vim set ft=make:
