include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 4.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 4c $<

go: 4.6
	$(GL) -o 4g $<

4.6: 4.go
	$(GC) 4.go

run: runpy runc rungo

runpy: 4.py
	python 4.py

runc: 4c
	./4c

rungo: 4g
	./4g

clean:
	rm -f 4c 4g 4.6

# :vim set ft=make:
