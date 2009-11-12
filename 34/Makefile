include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 34.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 34c $<

go: 34.6
	$(GL) -o 34g $<

34.6: 34.go
	$(GC) 34.go

run: runpy runc rungo

runpy: 34.py
	python 34.py

runc: 34c
	./34c

rungo: 34g
	./34g

clean:
	rm -f 34c 34g 34.6

# :vim set ft=make:
