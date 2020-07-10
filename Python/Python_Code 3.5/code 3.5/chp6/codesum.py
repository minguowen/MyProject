# codesum.py

def codesum1(s):
    """ Returns the sums of the character codes of s.
    """
    total = 0
    for c in s:
        total = total + ord(c)
    return total


def codesum2(s):
    """ Returns the sums of the character codes of s.
    """
    total = 0
    for i in range(len(s)):
        total = total + ord(s[i])
    return total
