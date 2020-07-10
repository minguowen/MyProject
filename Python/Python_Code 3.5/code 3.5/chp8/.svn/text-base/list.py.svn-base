# list.py

import os

def list_cwd():
    """ Returns a list of files and folders in the cwd.
    """
    return os.listdir(os.getcwd())

def files_cwd():
    """ Returns a list of the files in the cwd.
    """
    return [p for p in list_cwd()
            if os.path.isfile(p)]

def folders_cwd():
    """ Returns a list of the folders in the cwd.
    """
    return [p for p in list_cwd()
            if os.path.isdir(p)]

def list_py(path = None):
    """ Returns a list of all the file names ending with '.py'.
    If no path name is provided, then uses the cwd.
    """
    if path == None:
        path = os.getcwd()
    return [fname for fname in os.listdir(path)
            if os.path.isfile(fname)
            if fname.endswith('.py')]    

def size_in_bytes(fname):
    """ Returns the size, in bytes, of the named file.
    """
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    """ Returns the sum of the sizes of the files in cwd.
    Ignores directories.
    """
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total

def cwd_size_in_bytes2():
    """ Returns the sum of the sizes of the files in cwd.
    Ignores directories.
    """
    return sum(size_in_bytes(f) for f in files_cwd())

def cwd_size_in_kb():
    """ Returns size of cws in kilobytes.
    """
    return cwd_size_in_bytes() / 1024
