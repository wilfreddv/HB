CC=gcc
SRCS=$(wildcard src/*.c)
INCLUDES=$(wildcard include/*.h)
OBJS=$(SRCS:src/%.c=build/%.o)
CFLAGS=-c -Wall -Werror -pedantic -fPIC -O2 -g
LFLAGS=-shared

TARGET_LIB=libHB.so


.PHONY: install uninstall clean test
.DEFAULT: $(TARGET_LIB) 


$(TARGET_LIB): $(OBJS)
	$(CC) $(LFLAGS) -o $@ $^


build/%.o: src/*.c
	@mkdir -p build
	$(CC) $(CFLAGS) $< -o $@


install:

uninstall:


test: $(TARGET_LIB)
	$(CC) -L`pwd` -Wl,-rpath=`pwd` -Isrc/include/ test.c -o test -lHB
	./test

clean:
	rm -rf build/ *.so test
