def fib(x):
    """assumes x an int >= 0
    returns Fibonacci of x"""
    assert type(x) == int and x >= 0        # assert: checks the parameters, if true: executes, if false: returns error
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print fib(6)