include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 36.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 36c $<

go: 36.6
	$(GL) -o 36g $<

36.6: 36.go
	$(GC) 36.go

run: runpy runc rungo

runpy: 36.py
	python 36.py

runc: 36c
	./36c

rungo: 36g
	./36g

clean:
	rm -f 36c 36g 36.6

# :vim set ft=make:
