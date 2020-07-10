# allover.py

def is_done1(s):
    return s == 'done' or s == 'quit'

import re  # use regular expressions

def is_done2(s):
    return re.match('done|quit', s) != None

