# step size to skip number in a list
even_number = list(range(2, 11, 2))
print(even_number)

# make a list of the first 10 square number 
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
