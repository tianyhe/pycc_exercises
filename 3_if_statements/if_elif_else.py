# 5.2 - Alien Colors #1 
alien_color_1 = 'green'
if alien_color_1 == 'green':
    print('You just earnd 5 points')
if alien_color_1 == 'red':
    print('You are died')

# 5.3 - Alien Colors #2
alien_color_2 ='red'
if alien_color_2 != 'green':
    print('You just earned 10 points')
else:
    print('You are died')

# 5.4 - Alien Color #3
alien_color_3 = 'yellow'
pts = 0
if alien_color_3 == 'green':
    pts = 5
elif alien_color_3 == 'yellow':
    pts = 10
elif alien_color_3 == 'red':
    pts = 15
print(f'You just earned {pts} points')

# 5.5 - Stages of life
age = 18
if age < 2 :
    print('The person is a baby')
elif 2 <= age < 4:
    print('The person is a toddler')
elif 4 <= age < 13:
    print('The person is a kid')
elif 13 <= age < 20:
    print('The person is a teenager')
elif 20 <= age < 65:
    print('The person is an adult')
elif age >= 65:
    print('The person is an elder')

# 5.6 - Favorite Fruit
favorite_fruits = ['apple', 'banana', 'watermelon', 'lemon', 'strawberry']
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'banana' in favorite_fruits:
    print('You really like banana!')
if 'watermelon' in favorite_fruits:
    print('You really like watermelon!')
if 'lemon' in favorite_fruits:
    print('You really like lemon!')
if 'strawberry' in favorite_fruits:
    print('You really like strawberry!')
