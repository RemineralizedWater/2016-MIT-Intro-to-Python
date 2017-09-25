Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
print Techs
print Ivys[1]
print Ivys[:2]
Univs = [Techs, Ivys]       # Aliasing: two distinct paths to a data object (1: through variable Techs,
                            # 2: through 1st element of the list to which Univs is bound)
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
print Univs
print Univs1
Techs.append('RPI')     # appends 'RPI' as a new element to the end of Techs list
print Univs

Techs[2] = 'WPI'
print Univs

temp = ('one', 'two')
print temp[1]
# temp[1] = 'three'       # tuples, ints, strings, floats all are immutable

print Techs[0:1]          # the colon returns the element as type of it's container (in this case list type)


# REVIEW

print range(5)              # outputs list [0, 1, 2, 3, 4]
print range(2, 5)           # outputs list [2, 3, 4]
print range(2, 10, 2)       # outputs list [2, 4, 6, 8]
# print range(3, 10.5, 0.5)   # error, must be integers
print range(8, 2)           # outputs list []
print range (10, 3, -1)     # outputs list [10, 9, 8, 7, 6, 5, 4], starts at beginning of 10, ends at end of 3

print sum([1, 9, 10])       # outputs sum of list [1, 9, 10] = 20
print sum([4.5, 7, 0.331])  # outputs sum of list [4.5, 7, 0.331] = 11.831
# print sum(['a', 'b', 'c'])  # returns error


for e in Univs:                 # loop to each element in list
    print('Univs contains')
    print(e)
    print(' which contains')
    for u in e:                 # loop to print the internal elements of the list elements
        print('   ' + u)


flat = Techs + Ivys             # creating new version of the list
print flat
Techs.append(Ivys)              # mutating the same list
print Techs