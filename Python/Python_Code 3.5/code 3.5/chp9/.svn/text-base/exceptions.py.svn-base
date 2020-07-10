# exceptions.py

def get_age1():
    """ Returns an integer entered by the user.
    If the user enters a non-integer value, they
    are prompted again and again until they enter
    a valid integer.
    """
    while True:
        try:
            n = int(input('How old are you? '))
            return n
        except ValueError:
            print('Please enter an integer value.')

def convert_to_int1(s, base):
    """ Calls int(s, base), returning 'error' for exceptions.
    """
    try:
        return int(s, base)
    except (ValueError, TypeError):
        return 'error'

def convert_to_int2(s, base):
    """ Calls int(s, base), returning error strings for exceptions.
    """
    try:
        return int(s, base)
    except ValueError:
        return 'value error'
    except TypeError:
        return 'type error'

def convert_to_int3(s, base):
    """ Calls int(s, base), returning 'error' for exceptions.
    """
    try:
        return int(s, base)
    except:
        return 'error'

def invert(x):
    """ Returns 1/x.
    Returns an error of x is not a non-zero number.
    """
    try:
        return 1 / x
    except:
        return 'error'
    finally:
        print('invert(%s) done' % x)

def numbered_listing1(fname):
    """ Prints fname to the screen with numbered lines.
    """
    num = 1
    f = open(fname)
    for line in f:
        print('%04d %s' % (num, line), end = '')
        num = num + 1

def numbered_listing2(fname):
    """ Prints fname to the screen with numbered lines.
    """
    num = 1
    with open(fname) as f:
        for line in f:
            print('%04d %s' % (num, line), end = '')
            num = num + 1

def numbered_listing3(fname):
    """ Prints fname to the screen with numbered lines.
    """
    with open(fname) as f:
        for num, line in enumerate(f):
            print('%04d %s' % (num, line), end = '')

def numbered_listing4(fname):
    """ Prints fname to the screen with numbered lines.
    """
    with open(fname) as f:
        for num, line in enumerate(f):
            print('{0:04} {1}'.format(num, line), end = '')            

