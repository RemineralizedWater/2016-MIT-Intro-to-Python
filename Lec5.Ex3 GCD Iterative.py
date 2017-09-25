def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a > b:
        test = b
    elif a < b:
        test = a
    else:
        return a
    while a % test != 0 or b % test != 0:
        test -= 1
    return test

print gcdIter(10, 15)