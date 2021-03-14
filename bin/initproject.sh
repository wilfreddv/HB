#!/bin/bash

# `selector` needs to catch SIGTERM
fwdsigterm() { kill -TERM "$1" 2> /dev/null }

LANGUAGES=(
    Python
    C
    CPP
)

trap fwdsigterm $! 2
language=$(selector "Enter a language:" ${LANGUAGES[*]})
EXIT=$?
trap 2

if [[ $EXIT != "0" ]] ; then
    echo "Exiting..."
    exit 1
fi
