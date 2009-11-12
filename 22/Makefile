include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 22.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 22c $<

go: 22.6
	$(GL) -o 22g $<

22.6: 22.go
	$(GC) 22.go

run: runpy runc rungo

runpy: 22.py
	python 22.py

runc: 22c
	./22c

rungo: 22g
	./22g

clean:
	rm -f 22c 22g 22.6

# :vim set ft=make:
