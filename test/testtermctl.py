import sys
sys.path.append('../')

from pyutil.termctl import COLORS

print(COLORS.BOLD + COLORS.RED + COLORS.BLUEBG + "Hello red world!" + COLORS.END)