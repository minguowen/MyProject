# primes.py

def is_prime(n):
    """ Returns True if n is a prime number, and False otherwise.
    >>> is_prime(-7)
    False
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(25)
    False
    >>> is_prime(31)
    True
    """
    if n <= 1:
        return False
    elif n == 2:  # 2 is the only even prime
        return True
    else:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True
