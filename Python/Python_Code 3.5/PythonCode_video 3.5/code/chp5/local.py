# local.py

def dist(x, y, a, b):
    """ Distance between points (x, y) and (a, b).
    """
    import math
    s = (x - a) ** 2 + (y - b) ** 2
    return math.sqrt(s)

def rect_area(x, y, a, b):
    """ Returns the area of the given rectangle.
    Points (a, b) and (x, y) are diagonally opposite
    corners.
    """
    width = abs(x - a)
    height = abs(y - b)
    return width * height
