__author__ = 'Animatrix'

def max(x,y):
    '''
    Docstring goes here. Explain what type argument(s) should have, and what your function
   is going to return.
   '''
    if x > y:
        print(x)
        return x
    else:
        print(y)
        return y

z = max(3,4)

print(z)