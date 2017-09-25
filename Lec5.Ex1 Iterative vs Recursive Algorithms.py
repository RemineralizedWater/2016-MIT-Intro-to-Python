def iter_mul(a, b):                         # Iterative algorithm to do multiplication by addition
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


def recur_mul(a, b):                        # Recursive algorithm for same function as above
    if b == 1:
        return a
    else:
        return a + recur_mul(a, b-1)