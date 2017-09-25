def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)         # when remove element of a list being iterated over, python doesn't update list length

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print(L1)


def removeDupsBetter(L1, L2):
    L1Start = L1[:]                 # clone the list then iterate over clone to retain original list length
                                    # L1Start = L1 is not sufficient (because it points to original instead of copy)
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDupsBetter(L1, L2)
print(L1)


print L1 is L2                      # 'is' evaluates if one variable points to the other
