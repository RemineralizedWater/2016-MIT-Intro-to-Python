__author__ = 'Animatrix'

x = 12
c = 1


def g(x):

    c = 2    # local to g
    print x     # (12) local to g passed by reference
    print c     # (2) local value was set to 2
    x += 1
    print x     # (13) local statements change value locally

    def h(y):
        print c     # (2) local to h looked up from g
        print y     # (6) local to h passed by reference
        print x + y     # (19) x value here is looked up from g
        return x + y
    return h(6)
g(x)

print x     # (12) original x
print c     # (1)  outside of the function c remains untouched.