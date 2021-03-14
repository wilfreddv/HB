BINS=$(wildcard bin/*)


.PHONY: all install uninstall pyutil-install pyutil-uninstall
.DEFAULT: all
all:


install: pyutil-install
	cp -r share/ ~/.local/
	cp $(BINS) ~/.local/bin


uninstall: pyutil-uninstall
	rm -rf ~/.local/share/HB
	cd ~/.local; rm -f $(BINS)


pyutil-install: pyutil/
	python3 -m pip install .


pyutil-uninstall:
	python3 -m pip uninstall pyutil --yes
