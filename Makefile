.PHONY: all proj% clean

all:
	@echo "Usage: run make proj{ID} where {ID} is a project eueler problem id"

proj%:
	cd $(subst proj,,$@) && $(MAKE)

clean:
	@echo "Run make clean inside of each folder you'd like to clean"
