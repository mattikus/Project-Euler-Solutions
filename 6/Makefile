include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 6.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 6c $<

go: 6.6
	$(GL) -o 6g $<

6.6: 6.go
	$(GC) 6.go

run: runpy runc rungo

runpy: 6.py
	python 6.py

runc: 6c
	./6c

rungo: 6g
	./6g

clean:
	rm -f 6c 6g 6.6

# :vim set ft=make:
