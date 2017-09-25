def item_order(order):
    num_salad = order.count('salad')
    num_water = order.count('water')
    num_burger = order.count('hamburger')
    return 'salad:' + str(num_salad) + ' hamburger:' + str(num_burger) + ' water:' + str(num_water)

order1 = "salad water hamburger salad hamburger"
print item_order(order1)

order1 = "hamburger water hamburger"
print item_order(order1)