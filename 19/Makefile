include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 19.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 19c $<

go: 19.6
	$(GL) -o 19g $<

19.6: 19.go
	$(GC) 19.go

run: runpy runc rungo

runpy: 19.py
	python 19.py

runc: 19c
	./19c

rungo: 19g
	./19g

clean:
	rm -f 19c 19g 19.6

# :vim set ft=make:
