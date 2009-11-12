include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: 8.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o 8c $<

go: 8.6
	$(GL) -o 8g $<

8.6: 8.go
	$(GC) 8.go

run: runpy runc rungo

runpy: 8.py
	python 8.py

runc: 8c
	./8c

rungo: 8g
	./8g

clean:
	rm -f 8c 8g 8.6

# :vim set ft=make:
