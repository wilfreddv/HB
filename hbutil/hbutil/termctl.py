import sys
import termios, atexit, tty


class CTLSEQ:
    """
    Define common ANSI escape
    code control sequences
    """
    ESC = '\x1b'
    SCI     = ESC + '['
    K_UP    = SCI + 'A'
    K_DOWN  = SCI + 'B'
    K_RIGHT = SCI + 'C'
    K_LEFT  = SCI + 'D'
    BACKSPACE   = (chr(0x08), chr(0x7F))
    TERMINATOR  = ('\n', '\x04')

    C_UP    = SCI + "{}A"
    C_DOWN  = SCI + "{}B"
    C_RIGHT = SCI + "{}C"
    C_LEFT  = SCI + "{}D"


class _metacolors(type):
    def __init__(cls, *args, **kwargs):
        for name in dir(cls):
            if not name.startswith('_'):
                value = getattr(cls, name)
                setattr(cls, name, f"{CTLSEQ.SCI}{value}m")


class COLORS(metaclass=_metacolors):
    # Foreground
    BLACK       = 30
    RED         = 31
    GREEN       = 32
    YELLOW      = 33
    BLUE        = 34
    MAGENTA     = 35
    CYAN        = 36
    WHITE       = 37
    DEFAULT     = 38

    
    BBLACK      = 90
    BRED        = 91
    BGREEN      = 92
    BYELLOW     = 93
    BBLUE       = 94
    BMAGENTA    = 95
    BCYAN       = 96
    BWHITE      = 97

    # Background
    BLACKBG     = 40
    REDBG       = 41
    GREENBG     = 42
    YELLOWBG    = 43
    BLUEBG      = 44
    MAGENTABG   = 45
    CYANBG      = 46
    WHITEBG     = 47
    RESETBG     = 49

    BBLACKBG    = 100
    BREDBG      = 101
    BGREENBG    = 102
    BYELLOWBG   = 103
    BBLUEBG     = 104
    BMAGENTABG  = 105
    BCYANBG     = 106
    BWHITEBG    = 107

    # Other
    END         = 0
    BOLD        = 1
    DIM         = 2
    ITALIC      = 3
    UNDERLINE   = 4
    BLINK       = 5
    BLINKFAST   = 6
    INVERT      = 7
    HIDDEN      = 8
    STRIKE      = 9


class Terminal:
    """
    Wrapper for some terminal interactions
    """
    _STDIN = sys.stdin.fileno()


    def __init__(self, of=sys.stdout):
        self.old_termios = termios.tcgetattr(self._STDIN)
        self.termios = self.old_termios.copy()
        self.of = of 

        atexit.register(self.reset)


    def set_raw(self):
        """
        Set terminal to `raw`
        """
        tty.setcbreak(self._STDIN)

    
    def read(self, n=1):        
        c = self.getch(1)
        if c == CTLSEQ.ESC:
            return c + self.getch(2)
        else:
            c += self.getch(n-1)
        
        return c


    def write(self, data, clear_line=0, line_feed=0, newline=0):
        if line_feed:  data = "\r" + data
        if clear_line: data = data + f"{CTLSEQ.SCI}K"
        if newline: data += "\n"
        self.of.write(data)
        self.of.flush()

    
    def show_cursor(self):
        self.write(f"{CTLSEQ.SCI}?25h")

    def hide_cursor(self):
        self.write(f"{CTLSEQ.SCI}?25l")

    def move_cursor(self, distance, direction):
        self.write(direction.format(distance))


    def save_cursor(self):
        self.write(f"{CTLSEQ.ESC}[s")

    
    def restore_cursor(self):
        self.write(f"{CTLSEQ.ESC}[u")

    @staticmethod
    def getch(n=1):
        import sys
        return sys.stdin.read(n) if n else ""

    def reset(self):
        self.show_cursor()
        termios.tcsetattr(self._STDIN,
                          termios.TCSANOW,
                          self.old_termios)
