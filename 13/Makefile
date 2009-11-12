include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 13.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 13c $<

go: 13.6
	$(GL) -o 13g $<

13.6: 13.go
	$(GC) 13.go

run: runpy runc rungo

runpy: 13.py
	python 13.py

runc: 13c
	./13c

rungo: 13g
	./13g

clean:
	rm -f 13c 13g 13.6

# :vim set ft=make:
