listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print type(listA.sort())        # NoneType, with value None
print listA.sort()              # sorts the list in ascending order
print type(listA.insert(0, 100))      # NoneType, with value None
print listA.insert(0, 100)      # equivalent to appending 100 at position 0 (doesn't replace)
print listA.remove(3)           # var NoneType of value None (removes 3)
print listA.append(7)           # var NoneType of value None (appends 7 on end, as sub-list if multiple elements)
print listA.pop(4)              # removes item at position 4 from list, and returns it of type int
print listB.count('a')          # returns var int of the count of 'a'
# print listB.remove('a')         # returns var NoneType of value error due to trying to remove what isn't there
print listA.extend([4, 1, 6, 3, 4])     # returns var NoneType of value None (extends the list, not as sub-list)
print listA.count(4)            # returns var int of value 3 (counts the number of 4s)
print listA.index(1)            # var int of value 3 (finds index, but returns error if not found)
