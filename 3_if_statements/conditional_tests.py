# 5.1 - Conditional Tests
    # Test for equality and inequality with strings
car = 'Audi'
print("Is car == 'subaru'?")
print(car == 'subaru')
print("Is car != 'BMW'?")
print(car != 'BMW')

    # Test using lower() Method
print("Is car == 'audi'?")
print(car.lower() == 'audi')

    # Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to 
rico = 21
liz = 18
if rico != 21: 
    print('Rico is not 21 years old')
if liz == 18: 
    print('Liz is 18 years old')
if rico > 18: 
    print('Rico is more than 18 years old')
if liz < 21: 
    print('Liz is under 21 years old')
if rico >= 18: 
    print('Rico is at least 18 years old')
if liz <= 21: 
    print('Liz is no more than 21 years old')

    # Tests suing the 'and' keyword and the 'or' keyword
if rico >= 18 and liz >= 18: 
    print('Rico and Liz are both at least 18 years old')
if rico < 21 or liz < 21: 
    print('At least one them are under 21 years old')  

    # Test whether an item is in a list
pizzas = ['hawaiian', 'pepperoni', 'mozeralla']
if 'hawaiian' in pizzas: 
    print('hawaiian is one of my favorite pizzas')
    # Test whether an item is not in a list
if 'four seasons' not in pizzas: 
    print('four season is not one of my favorite pizza')

