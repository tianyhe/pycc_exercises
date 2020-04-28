# 6.7 - People
liz = {'first_name': 'liz', 'last_name': 'zheng', 'age': 22, 'city': 'shanghai'}
joanne = {'first_name': 'joanne', 'last_name': 'chan', 'age': 25, 'city': 'taiwan'}
jessica = {'first_name': 'jessica', 'last_name': 'xing', 'age': 25, 'city': 'hongkong'}

people = [liz, joanne, jessica]
for babe in people:
    full_name = f"{babe['first_name']} {babe['last_name']}"
    print('\n', full_name.title())
    print('\tAges:', babe['age'])
    print('\tCity:', babe['city'].title())

# 6.8 - Pets
timo = {'animal': 'cat', 'owner': 'liz'}
hamburger = {'animal': 'dog', 'owner': 'evelyn'}
mimi = {'animal': 'cat', 'owner': 'timo'}

pets = [timo, hamburger, mimi]
for pet in pets:
    print(f"\nType of animal: {pet['animal']} Owner: {pet['owner']}")

# 6.9 - Favorite Places
favorite_places = {
    'liz': ['barcelona', 'lausanne', 'los angles'],
    'joanne': ['barcelona', 'japan', 'hongkong'],
    'jessica': ['amsterdam', 'bangkok', 'paris'],
    'aliey' : ['shanghai']
}

for babe, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{babe.title()} favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{babe.title()} favorite places is:\n\t{places[0].title()}")

# 6.10 - Favorite Numbers
favorite_number = {
    'liz': [617, 821],
    'rico': [821, 617],
    'batu': [420, 911],
    'chasel': [1016, 420],
    'jessica': [99, 520]
}
for ppl, nums in favorite_number.items():
    print(f"\n{ppl.title()}'s favorite numbers are:", end=' ')
    for num in nums:
        print(num, end=' ')
print('')
# 6.11 - Cities
cities = {
    'barcelona': {
        'country': 'spain',
        'population': 5_575_000,
        'fact': 'The cosmopolitan capital of Spain’s Catalonia region, is known for its art and architecture.'
    },
    'amsterdam': {
        'country': 'netherlands',
        'population': 821_752,
        'fact': 'Amsterdam is the Netherlands’ capital.'
    },
    'los angles': {
        'country': 'america',
        'population': 4_000_000,
        'fact': 'Los Angeles is a sprawling Southern California city and the center of the nation’s film and television industry.'
    }
}

for city, info in cities.items():
    print(f"\nName of the city: {city.title()}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")

