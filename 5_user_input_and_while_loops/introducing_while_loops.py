# 7.4 & 7.6 - Pizza Topping (Three Exits)
prompt = 'Please enter the toppings you would like: (Maximum # of toppings: 3)'
prompt += "\n(Enter 'quit' when you are finished.)\n"
num = 1
allow = True
while num <= 3 and allow:
    topping = input(prompt)
    if topping == 'quit':
        break # Exit 1 - break statement
    if len(topping) > 0:
        print(f"The '{topping}' were added to the pizza ({3 - num} left)'")
        num += 1 # Exit 2 - conditional test
    else:
        print('No topping added')
        allow = False # Exit 3 - flag

# 7.5 & 7.6 - Movie Tickets (Three Exits)
prompt = 'Please enter your age to check the ticket price (rate limits = 5)'
prompt += "\n(Enter 'quit' to exit the program.)\n"
rate = 1
active = True
while rate <= 5 and active:
    age = input(prompt)
    if age == 'quit':
        break # Exit 1 - break statement
    try:
        age = int(age)
        if int(age) < 3:
            print(f'The ticket is free. ({5 - rate} left)')
        elif 3 <= int(age) <= 12:
            print(f'The ticket is $10. ({5 - rate} left)')
        elif int(age) > 12:
            print(f'The ticket is $15. ({5 - rate} left)')
        rate += 1 # Exit 2 - conditional test
    except:
        active = False # Exit 3 - flag

# 7.7 - Infinity
x = 1
while x > 0:
    print(x)




