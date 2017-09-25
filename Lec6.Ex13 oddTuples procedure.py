def oddTuples(aTup):
    """
    :param aTup: a tuple
    :return: tuple, every other element of aTup.
    """
    oddTup = ()
    i = 0
    while i < len(aTup):
            if i % 2 == 0:
                print tuple(aTup[i])
                oddTup += (aTup[i],)
                print oddTup
            i += 1
    return oddTup


aTup = ('I', 'am', 'a', 'test', 'tuple')
print aTup[4]
print len(oddTuples(aTup))
