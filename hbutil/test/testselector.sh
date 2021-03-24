MYVAR="$(../hbutil/selector.py "Enter something:" `shuf -n 500000 /usr/share/dict/american-english`)"
echo $MYVAR
