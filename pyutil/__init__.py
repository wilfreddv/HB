from pyutil.grep import grep
from pyutil.termctl import Terminal


def getch(n=1):
    import sys
    return sys.stdin.read(n) if n else ""