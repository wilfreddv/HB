class grep:
    """
    Search for matching patterns
    `list or newline seperated strings` | grep(pattern, E=False)
    -> list of items that matched the pattern

    The `i` flag enables case insensitive search

    The `E` argument enables regex mode
    (much like the -E flag for the grep utility)
    """
    def __init__(self, match, i=False, E=False):
        self.E = E
        self.i = i
        
        if E:
            import re
            self.match = re.compile(match)
        else:
            self.match = match
            if self.i: self.match = self.match.lower()
            

    def __ror__(self, other):
        if type(other) == str:
            other = other.split('\n')
        else:
            other = list(map(str, other))


        if self.E:
            f = lambda t: self.match.match(t)
        else:
            f = lambda t: self.match in t
            if self.i:
                f = lambda t: self.match in t.lower()

            
            
        return list(filter(f, other))
