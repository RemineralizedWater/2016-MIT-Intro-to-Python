def item_order(order):
    num_salad = 0
    num_ham = 0
    num_water = 0
    for i in range(0, len(order)-4):
        if order[i: i+5] == 'salad':
            num_salad += 1
        elif order[i: i+9] == 'hamburger':
            num_ham += 1
        elif order[i: i+5] == 'water':
            num_water += 1
    return 'salad:' + str(num_salad) + ' hamburger:' + str(num_ham) + ' water:' + str(num_water)

order1 = "salad water hamburger salad hamburger"
print item_order(order1)

order1 = "hamburger water hamburger"
print item_order(order1)