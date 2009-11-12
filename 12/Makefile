include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 12.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 12c $<

go: 12.6
	$(GL) -o 12g $<

12.6: 12.go
	$(GC) 12.go

run: runpy runc rungo

runpy: 12.py
	python 12.py

runc: 12c
	./12c

rungo: 12g
	./12g

clean:
	rm -f 12c 12g 12.6

# :vim set ft=make:
