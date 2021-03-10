.PHONY: all install uninstall pyutil
.DEFAULT: all
all:


install:
	make pyutil


uninstall:
	python3 -m pip uninstall pyutil


pyutil: pyutil/
	python3 -m pip install .
