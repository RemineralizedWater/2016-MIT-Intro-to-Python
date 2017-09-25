from math import *                              # import math module to enable usage of tan and pi


def polysum(n, s):
    area = (0.25 * n * s**2)/tan(pi/n)          # calculates area of polygon
    perimeter = n * s                           # calculates perimeter of polygon
    return round(area + perimeter**2, 4)        # returns polysum = area + perimeter ** 2, then rounds to 4 decimals