include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 17.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 17c $<

go: 17.6
	$(GL) -o 17g $<

17.6: 17.go
	$(GC) 17.go

run: runpy runc rungo

runpy: 17.py
	python 17.py

runc: 17c
	./17c

rungo: 17g
	./17g

clean:
	rm -f 17c 17g 17.6

# :vim set ft=make:
