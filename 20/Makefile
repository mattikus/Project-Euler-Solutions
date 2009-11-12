include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 20.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 20c $<

go: 20.6
	$(GL) -o 20g $<

20.6: 20.go
	$(GC) 20.go

run: runpy runc rungo

runpy: 20.py
	python 20.py

runc: 20c
	./20c

rungo: 20g
	./20g

clean:
	rm -f 20c 20g 20.6

# :vim set ft=make:
