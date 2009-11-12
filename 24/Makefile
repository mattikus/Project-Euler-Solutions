include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 24.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 24c $<

go: 24.6
	$(GL) -o 24g $<

24.6: 24.go
	$(GC) 24.go

run: runpy runc rungo

runpy: 24.py
	python 24.py

runc: 24c
	./24c

rungo: 24g
	./24g

clean:
	rm -f 24c 24g 24.6

# :vim set ft=make:
