def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    
    start_space = 0
    space = 0
    while space > -1:
        space = order.find(' ', start_space)        # function str.find returns -1 when no more spaces, so loop ends
        print space
        if space == -1:
            word = order[start_space:]              # determines if this is the last word and sets to word
            print word
        else:
            word = order[start_space:space]         # otherwise sets word to start of word to next space - 1
        if word == "salad":
            salad += 1
        if word == "hamburger":
            hamburger += 1
        if word == "water":
            water += 1
        start_space = space+1                       # sets the start of the next word
    new_order = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return new_order

order1 = "salad water hamburger salad hamburger"
print item_order(order1)

order1 = "hamburger water hamburger"
print item_order(order1)