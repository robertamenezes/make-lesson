include config.mk

TXT_FILES=$(wildcard books/*.txt)

analysis.tar.gz : *.dat $(COUNT_SRC)
	tar -czf $@ $^

.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)

.PHONY : dats
dats : isles.dat abyss.dat last.dat

%.dat : books/%.txt $(COUNT_SRC)
	$(COUNT_EXE) $< $*.dat

.PHONY : clean
clean : 
	rm -f *.dat  
	rm -f analysis.tar.gz
