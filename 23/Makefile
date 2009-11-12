include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 23.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 23c $<

go: 23.6
	$(GL) -o 23g $<

23.6: 23.go
	$(GC) 23.go

run: runpy runc rungo

runpy: 23.py
	python 23.py

runc: 23c
	./23c

rungo: 23g
	./23g

clean:
	rm -f 23c 23g 23.6

# :vim set ft=make:
