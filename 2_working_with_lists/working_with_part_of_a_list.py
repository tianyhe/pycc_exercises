# 4.10 - Slices
locations = ['barcelona', 'montreux', 'amsterdam', 'los angles', 'cuba']
print('The first threee items in the list are:', locations[:3])
print('Three items from the middle of the list are:', locations[1:4])
print('The last three items in the list are:', locations[-3:])

# 4.11 - My Pizzas, Your Pizzas
my_pizzas = ['Mozeralla', 'Hawaiian', 'Four Cheese']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Pepperoni')
friend_pizzas.append('Four Seasons')
print('\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4.12 - Buffet
menu = ('egg', 'water', 'rice', 'beef', 'pork')
print('Origina menu:\n')
for food in menu:
    print(food)
menu = ('egg', 'water', 'rice', 'chicken', 'lamb')
print('Revised Menu:\n')
for food in menu:
    print(food)