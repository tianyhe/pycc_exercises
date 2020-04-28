# 6.1 - Person
liz = {'first_name': 'Liz', 'last_name': 'Zheng', 'age': 22, 'city': 'Shanghai'}
print(liz['first_name'])
print(liz['last_name'])
print(liz['age'])
print(liz['city'])

# 6.2 - Favorite Numbers
favorite_number = {
    'liz': 617,
    'rico': 821,
    'batu': 420,
    'chasel': 1016,
    'jessica': 99,
}
print(favorite_number['liz'])
print(favorite_number['rico'])
print(favorite_number['batu'])
print(favorite_number['chasel'])
print(favorite_number['jessica'])

# 6.3 - Glossary
glossary = {
    'variable': 'Every variable is connected to a value, which is the information associated with that variable.',
    'string': 'A string is a series of characters.',
    'float': 'Any number with a decimal point is a float.',
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.'
}
print('\nvariable:', glossary.get('variable'))
print('\nstring:', glossary.get('string'))
print('\nfloat:', glossary.get('float'))
print('\nlist:', glossary.get('list'))
print('\ndictionary:', glossary.get('dictionary'))