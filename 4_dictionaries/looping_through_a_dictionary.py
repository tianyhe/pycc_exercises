# 6.4 - Glossary 2
glossary = {
    'variable': 'Every variable is connected to a value, which is the information associated with that variable.',
    'string': 'A string is a series of characters.',
    'float': 'Any number with a decimal point is a float.',
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.',
    'set': 'A set is acollection in which each item must be unique'
}

for key, value in glossary.items():
    print(f'{key}: {value}\n')

# 6.5 - Rivers
rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'donau': 'germany'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}\n')
for river in rivers.keys():
    print('Name of the river:', river.title(), '\n')
for country in rivers.values():
    print('Name of the country:', country.title(), '\n')

# 6.6 - Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['jen', 'sarah', 'liz', 'joanne', 'jessica']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f'Hi {friend.title()}! Thank you for responding, love you!')
    else:
        print(f'{friend.title()} babe, please take the poll.')
