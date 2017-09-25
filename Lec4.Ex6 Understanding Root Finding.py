__author__ = 'Animatrix'


def find_root1(x, power, epsilon):
    ''' x and epsilon int or float, power an int
        epsilon > 0 & power >= 1
        returns a float y s t. y**power is within epsilon of x.
        If such a float does not exist, it returns None '''
    if x < 0 and power % 2 == 0:
        return None     # Can't find even powered root of negative number
    low = min(-1, x)     # Test for positive/negative and if between 0 and 1/-1
    high = max(1, x)    # Test for positive/negative and if between 0 and 1/-1
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        print ans
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

find_root1(.25, 3, 0.001)