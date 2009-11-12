include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 30.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 30c $<

go: 30.6
	$(GL) -o 30g $<

30.6: 30.go
	$(GC) 30.go

run: runpy runc rungo

runpy: 30.py
	python 30.py

runc: 30c
	./30c

rungo: 30g
	./30g

clean:
	rm -f 30c 30g 30.6

# :vim set ft=make:
