# 2.3 - Personal Message
name = 'Rico'
print(f'Hello {name}, would you like to learn some Python today?')

# 2.4 - Name Cases
name = 'Rico'
print(name.upper())
print(name.lower())
print(name.title())

# 2.5 - Famous Quote
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(quote)

# 2.6 - Famous Quote 2
famous_person = 'Albert Einstein'
quote = 'A person who never made a mistake never tried anything new'
message = f'{famous_person} once said, "{quote}"'
print(message)

# 2.7 - Stripping Names
my_name = "\n\tRico Tianyao He\n"
print('original text:', my_name)
print('lstrip:', my_name.lstrip())
print('rstrip', my_name.rstrip())
print('strip:', my_name.strip())