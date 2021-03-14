.PHONY: all install uninstall pyutil-install pyutil-uninstall
.DEFAULT: all
all:


install:
	make pyutil-install


uninstall:
	make pyutil-uninstall


pyutil-install: pyutil/
	python3 -m pip install .

pyutil-uninstall:
	python3 -m pip uninstall pyutil
