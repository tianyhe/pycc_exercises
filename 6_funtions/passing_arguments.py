# 8.3 - T-Shirts
def make_shirt(size, message):
    """accepts a size and the text of the message that should printed on the shirt, then print a sentence summarizing the information"""
    print(f"\nThe size of the T-shirt is {size}.")
    print(f"The message should printed on the shirt is '{message}'.")
    # positional arguments
make_shirt('Large', 'Rico')
    # keywords arguments
make_shirt(message='Liz', size='Small')

# 8.4 - Large Shirts
def make_shirt_default(size='Large', message='I love Python'):
    """make_shirt function with default size value and message value"""
    print(f"\nThe size of the T-shirt is {size}.")
    print(f"The message should printed on the shirt is '{message}'.")

make_shirt_default()
make_shirt_default(size='Medium')
make_shirt_default(size='Small', message='I love Computer Science')

# 8.4 - Cities
def describe_city(city, country='China'):
    """accepts the name of the city and its country then print a simple sentence. The default value of country is China."""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('guangzhou')
describe_city('shanghai')
describe_city('lausanne', country='Switzerland')
describe_city(city='Geneva', country='switzerland')