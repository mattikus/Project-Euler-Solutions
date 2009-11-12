include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 2.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 2c $<

go: 2.6
	$(GL) -o 2g $<

2.6: 2.go
	$(GC) 2.go

run: runpy runc rungo

runpy: 2.py
	python 2.py

runc: 2c
	./2c

rungo: 2g
	./2g

clean:
	rm -f 2c 2g 2.6

# :vim set ft=make:
