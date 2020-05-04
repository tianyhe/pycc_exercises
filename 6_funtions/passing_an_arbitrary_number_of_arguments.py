# 8.12 - Sandwiches
def make_sandwiches(*items):
    """Summarize the sandwiches we are about to make"""
    print(f"\nMaking a sandwiches with the following topping:")
    for item in items:
        print(f"- {item}")

make_sandwiches('tomato', 'cheese', 'bacon', 'beef')
make_sandwiches('watermelon', 'pork')
make_sandwiches('lamb', 'love', 'caring')

# 8.13 - User Profiles
def build_profile(first_name, last_name, **user_info):
    """Build a dictionary about everything we know about a user"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

profile = build_profile('Rico', 'He', location='Shanghai', age='23', school='EHL')
print(f"\n{profile['first_name']}'s Profile: ", profile)

# 8.14 - Cars
def make_car(manufacturer, model, **kwargs):
    """Build a dictionary about everything we know about a car"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print('\nInfo of the car:', car)
