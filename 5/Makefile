include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 5.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 5c $<

go: 5.6
	$(GL) -o 5g $<

5.6: 5.go
	$(GC) 5.go

run: runpy runc rungo

runpy: 5.py
	python 5.py

runc: 5c
	./5c

rungo: 5g
	./5g

clean:
	rm -f 5c 5g 5.6

# :vim set ft=make:
