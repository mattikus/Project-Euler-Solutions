include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 1.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 1c $<

go: 1.6
	$(GL) -o 1g $<

1.6: 1.go
	$(GC) 1.go

run: runpy runc rungo

runpy: 1.py
	python 1.py

runc: 1c
	./1c

rungo: 1g
	./1g

clean:
	rm -f 1c 1g 1.6

# :vim set ft=make:
