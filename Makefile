include ../Makefile.include

.PHONY: run runpy runc rungo clean

all: c go

c: ..c
	$(CC) $(CFLAGS) $(LDFLAGS) -o .c $<

go: ..6
	$(GL) -o .g $<

..6: ..go
	$(GC) ..go

run: runpy runc rungo

runpy: ..py
	python ..py

runc: .c
	./.c

rungo: .g
	./.g

clean:
	rm -f .c .g ..6

# :vim set ft=make:
