include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 18.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 18c $<

go: 18.6
	$(GL) -o 18g $<

18.6: 18.go
	$(GC) 18.go

run: runpy runc rungo

runpy: 18.py
	python 18.py

runc: 18c
	./18c

rungo: 18g
	./18g

clean:
	rm -f 18c 18g 18.6

# :vim set ft=make:
