def gcd(x, y):
    while x % y != 0:
        temp = x % y
        x, y = y, temp
    return y

print(gcd(30,15))