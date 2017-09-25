__author__ = 'Animatrix'

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(hi,max(x, lo))   # returns the min or max of a set of arguments