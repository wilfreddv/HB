#!/bin/bash

cd ../pyutil
echo $PWD
export PYTHONPATH=$(realpath ../):$PYTHONPATH
shuf -n 200 /usr/share/dict/american-english | ./selector.py "Enter something:"
