# Make File Template

CXX = g++
CXX_FLAGS = -g -Wall

INCL_DIR =
LIB_DIR =
LD_FLAGS = ${LIB_DIR}

CXX_FILES = #Use Wildcard If required
HEADERS =
OBJ_FILES = $(CXX_FILES:.cpp=.o)
TARGET = main

all: run

${TARGET}: ${OBJ_FILES}
	${CXX} -o $@ $^ ${LD_FLAGS}

run: ${TARGET}
	./${TARGET}

clean: ${TARGET} ${OBJ_FILES}
	rm $^


