def fact_i(n):                                  # iterative factorial algorithm
    """ assumes that n is an int > 0
    returns n! """
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res


def fact_r(n):                                  # recursive factorial algorithm
    """ assumes that n is an int > 0
    returns n! """
    if n == 1:
        return n
    return n * fact_r(n-1)