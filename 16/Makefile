include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 16.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 16c $<

go: 16.6
	$(GL) -o 16g $<

16.6: 16.go
	$(GC) 16.go

run: runpy runc rungo

runpy: 16.py
	python 16.py

runc: 16c
	./16c

rungo: 16g
	./16g

clean:
	rm -f 16c 16g 16.6

# :vim set ft=make:
