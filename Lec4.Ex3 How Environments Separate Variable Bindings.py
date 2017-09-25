__author__ = 'Animatrix'

def square(x):
    return x**2

def twoPower(x, n):
    while n > 1:
        x = square(x)
        n = n/2
    return x

print(square(4.2))
print(twoPower(2, 8))