import sys
sys.path.append('../')

from hbutil.termctl import COLORS

print(COLORS.BOLD + COLORS.RED + COLORS.BLUEBG + "Hello red world!" + COLORS.END)
