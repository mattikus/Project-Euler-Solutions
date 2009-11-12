include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 21.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 21c $<

go: 21.6
	$(GL) -o 21g $<

21.6: 21.go
	$(GC) 21.go

run: runpy runc rungo

runpy: 21.py
	python 21.py

runc: 21c
	./21c

rungo: 21g
	./21g

clean:
	rm -f 21c 21g 21.6

# :vim set ft=make:
