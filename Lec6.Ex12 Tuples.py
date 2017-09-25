t1 = (1, 'two', 3)
print(t1)
print len(t1)
t2 = (t1, 'four')
print(t1+t2)
print(t1+t2)[3]
print(t1+t2)[2:5]
t3 = ('five',)
print(t1+t2+t3)


def find_divisors(n1, n2):
    """assume n1 and n2 positive ints
        returns tuple containing
            common divisors of n1 and n2"""
    divisors = ()   # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors += (i,)
    return divisors

divs = find_divisors(20, 100)
total = 0
for d in divs:
    total += d

print(total)

print 'John' [1][0]

x = (1, 2, (3, 'John', 4), 'Hi')

print x[0:1]

print type(x[2])
print x[2]

print type(x[-1])
print x[-1]

print type(x[2][2])     # second index is for the tuple inside the tuple
print x[2][2]           # thus it is element 2 in element 2

print type(x[2][-1])    # second element of outside tuple, -1st element of inside tuple
print x[2][-1]

print type(x[-1][-1])   # string
print x[-1][-1]         # final character of last tuple element

# print type(x[-1][2])  # NoneType due to only being two characters
# print x[-1][2]        # error due to not existing

print type(x[0:-1])

print(len(x))

print 2 in x            # outputs True

print 3 in x            # outputs False

# x[0] = 8              # tuples don't support item assignment, so creates error
