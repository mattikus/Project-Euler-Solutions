include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 9.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 9c $<

go: 9.6
	$(GL) -o 9g $<

9.6: 9.go
	$(GC) 9.go

run: runpy runc rungo

runpy: 9.py
	python 9.py

runc: 9c
	./9c

rungo: 9g
	./9g

clean:
	rm -f 9c 9g 9.6

# :vim set ft=make:
