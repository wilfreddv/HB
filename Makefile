BINS=$(wildcard bin/*)
SUBDIRS=hbutil

.PHONY: all install uninstall
.DEFAULT: all
all:


install: $(SUBDIRS)
	$(MAKE) -C hbutil install
	
	cp -r share/ ~/.local/
	cp $(BINS) ~/.local/bin


uninstall: $(SUBDIRS)
	$(MAKE) -C hbutil uninstall
	
	rm -rf ~/.local/share/HB
	cd ~/.local; rm -f $(BINS)
