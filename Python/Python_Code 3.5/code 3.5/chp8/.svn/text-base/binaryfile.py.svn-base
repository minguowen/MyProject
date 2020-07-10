# binaryfile.py

def is_gif(fname):
    """ Returns True just when fname is a GIF file.
    Checks the first 4 bytes of the given to see if
    they match the "magic number" for GIF files.
    The magic number for a GIF file in hexadecimal is:

        0x47 0x49 0x46 0x38
    """
    f = open(fname, 'br')
    first4 = tuple(f.read(4))
    return first4 == (0x47, 0x49, 0x46, 0x38)
    
