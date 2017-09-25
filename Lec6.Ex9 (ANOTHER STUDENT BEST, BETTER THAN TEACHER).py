def isIn(char, aStr):
    if aStr == '':
        return False
    elif char == aStr[len(aStr)/2]:
        return True
    elif char > aStr[len(aStr)/2]:
        return isIn(char, aStr[len(aStr)/2+1:])
    else:
        return isIn(char, aStr[:len(aStr)/2])

print isIn('f', 'abcfg')
print 'ab'[0:1]
print 1/2
test = 'a'
print test[len(test)/2]
print len(test)/2