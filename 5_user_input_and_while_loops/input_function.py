# 7.1 - Rental Car
car = input('What kind of rental car you would like?\n')
print(f"Let me see if i can find you a {car}.")

# 7.2 - Restaurant Seating
ppl = input('How many people are in your dinner group?\n')
ppl = int(ppl)
if ppl > 8:
    print('You will have to wait for a table')
else:
    print('The table is ready')

# 7.3 - Mutiples of Ten
num = input('Please enter a number:\n')
rm = int(num) % 10
if rm != 0:
    print('The number is not a mutiple of 10')
else:
    print('The number is a mutiple of 10')