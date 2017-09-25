__author__ = 'Animatrix'

import circle   # import method 1 (used when have global variables don't want overridden)


pi = 3.0
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))


def area(x):
    return x**2

print(area(3))      # Prior to importing circle.area


from circle import *    # import method 2 (overrides global variables & allows calls with/without dot method)

print(pi)
pi = 0.0
print(pi)
print(area(3))
print(circle.pi)


def area(x):
    return x**2

print(area(3))      # After to importing circle.area