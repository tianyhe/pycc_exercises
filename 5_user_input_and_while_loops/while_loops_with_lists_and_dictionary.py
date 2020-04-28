# 7.8 - Deli
sandwich_orders = ['tuna sandwich', 'pastrami sandwich','chicken sandwich','chicken sandwich', 'pastrami sandwich', 'beef sandwich', 'pork sandwich', 'chicken sandwich','pastrami sandwich','lamb sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print('The following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(sandwich)

# 7.9 - No Pastrami
print('\nThe deli has run out of pastrami.')
sandwich_orders = ['tuna sandwich', 'pastrami sandwich','chicken sandwich','chicken sandwich', 'pastrami sandwich', 'beef sandwich', 'pork sandwich', 'chicken sandwich','pastrami sandwich','lamb sandwich']
finished_sandwiches = []
    # Alternative approach to remove pastrami sandwiches from the orders
# while 'pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove('pastrami sandwich')
# print(sandwich_orders)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami sandwich':
        print('Sorry, we run out of pastrami.')
        continue
    else:
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)
print('The following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(sandwich)

# 7.10 - Dream Vacation
responses = {}
polling_active = True
name_prompt = '\nWhat is your name? '
location_prompt = 'If you could visit one place in the world, where would you go? '
repeat_prompt = 'Would you like another person to response? (yes/no)'
while polling_active:
    # Prompt for the person's name and response
    name = input(name_prompt)
    location = input(location_prompt)
    # Store the response in the dictionary
    responses[name] = location
    # Find out if anyone else is going to take the poll
    repeat = input(repeat_prompt)
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results:
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f"{name.title()}: {response.title()}")
