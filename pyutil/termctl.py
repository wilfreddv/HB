import sys
import termios, atexit, tty
from pyutil import getch


class Terminal:
    """
    Wrapper for some terminal interactions
    """
    _STDIN = sys.stdin.fileno()
    ESC = '\x1b'
    SCI = f'{ESC}['
    K_UP = f"{SCI}A"
    K_DOWN = f"{SCI}B"
    K_RIGHT = f"{SCI}C"
    K_LEFT = f"{SCI}D"
    BACKSPACE = (chr(0x08), chr(0x7F))
    TERMINATOR = ('\n', '\x04')

    C_UP    = f"{SCI}{{}}A"
    C_DOWN  = f"{SCI}{{}}B"
    C_RIGHT = f"{SCI}{{}}C"
    C_LEFT  = f"{SCI}{{}}D"

    def __init__(self):
        self.old_termios = termios.tcgetattr(self._STDIN)
        self.termios = self.old_termios.copy()
        
        atexit.register(self.reset)


    def set_raw(self):
        """
        Set terminal to `raw`
        """
        tty.setcbreak(self._STDIN)

    
    def read(self, n=1):        
        c = getch(1)
        if c == Terminal.ESC:
            return c + getch(2)
        else:
            c += getch(n-1)
        
        return c


    def write(self, data, clear_line=0, line_feed=0, newline=0):
        if line_feed:  data = "\r" + data
        if clear_line: data = data + f"{self.SCI}K"
        if newline: data += "\n"
        sys.stdout.write(data)
        sys.stdout.flush()

    
    def show_cursor(self):
        self.write(f"{self.SCI}?25h")

    def hide_cursor(self):
        self.write(f"{self.SCI}?25l")

    def move_cursor(self, distance, direction):
        self.write(direction.format(distance))


    def save_cursor(self):
        self.write(f"{self.ESC}[s")

    
    def restore_cursor(self):
        self.write(f"{self.ESC}[u")


    def reset(self):
        self.show_cursor()
        termios.tcsetattr(self._STDIN,
                          termios.TCSANOW,
                          self.old_termios)