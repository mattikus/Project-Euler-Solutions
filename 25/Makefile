include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 25.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 25c $<

go: 25.6
	$(GL) -o 25g $<

25.6: 25.go
	$(GC) 25.go

run: runpy runc rungo

runpy: 25.py
	python 25.py

runc: 25c
	./25c

rungo: 25g
	./25g

clean:
	rm -f 25c 25g 25.6

# :vim set ft=make:
