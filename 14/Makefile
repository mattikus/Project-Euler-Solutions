include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 14.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 14c $<

go: 14.6
	$(GL) -o 14g $<

14.6: 14.go
	$(GC) 14.go

run: runpy runc rungo

runpy: 14.py
	python 14.py

runc: 14c
	./14c

rungo: 14g
	./14g

clean:
	rm -f 14c 14g 14.6

# :vim set ft=make:
