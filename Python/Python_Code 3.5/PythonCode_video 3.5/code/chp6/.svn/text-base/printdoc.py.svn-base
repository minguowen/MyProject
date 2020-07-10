# printdoc.py

def doc(fn):
    """Prints fn's doc string.
    """
    print(getattr(fn, '__doc__'))

def string_doc():
    members = [n for n in dir('') if not n.startswith('_')]
    for name in members:
        fn = getattr('', name)
        d = getattr(fn, '__doc__')
        print('  %s\n%s\n' % (name, d))

def print_doc(obj):
    members = [n for n in dir(obj) if not n.startswith('_')]
    for name in members:
        fn = getattr(obj, name)
        d = getattr(fn, '__doc__')
        print('%s\n%s\n\n' % (name, d))
    
