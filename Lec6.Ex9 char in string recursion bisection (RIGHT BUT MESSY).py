def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if aStr == '':
        return False

    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False

    elif len(aStr) % 2 == 1:
        if char == aStr[len(aStr)/2:len(aStr)/2+1]:
            return True
        elif char < aStr[len(aStr)/2:len(aStr)/2+1]:
            return isIn(char, aStr[:len(aStr)/2])
        else:
            return isIn(char, aStr[len(aStr)/2+1:])

    else:
        if char == aStr[(len(aStr)/2)-1:len(aStr)/2]:
            return True
        elif char < aStr[(len(aStr)/2)-1:len(aStr)/2]:
            return isIn(char, aStr[:len(aStr)/2-1])
        else:
            return isIn(char, aStr[len(aStr)/2:])

print isIn('h', 'abcdefgijklmnop')