def gcdRecur(a, b):
    """
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    """
    '''
    if a < b:
        temp = b
        b = a
        a = temp                # unnecessary due to if A < B, then A % B = A
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)