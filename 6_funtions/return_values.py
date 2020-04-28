# 8.6 - City Names
def city_country(city, country):
    """Return a neatly formatted string with city and country"""
    msg = f"{city}, {country}"
    return msg

pairs = city_country('Santiago', 'Chile')
print(pairs)
pairs = city_country('Los Angles', 'USA')
print(pairs)
pairs = city_country('Shanghai', 'China')
print(pairs)

print('\n')

# 8.7 - Album
def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary of information about an album"""
    if number_of_songs:
        album = {'name': artist_name, 'title': album_title, 'numbers': number_of_songs}
    else:
        album = {'name': artist_name, 'title': album_title}
    return album

album_1 = make_album('Rico', 'I love Computer Science')
print(album_1)
album_2 = make_album('Liz', 'I love Interior Design')
print(album_2)
album_3 = make_album('Batu', 'I got a babe', '3')
print(album_3)

# 8.8 - User Albums
while True:
    print('\nPlease fill out the information of the album:')
    print("(Enter 'q' at any time to quit)")
    a_name = input('Please enter the name of the artist: ')
    if a_name == 'q':
        break
    a_title = input('Please enter the name of the album: ')
    if a_title == 'q':
        break
    n_songs = input('Please enter the numbers of songs in the album: ')
    if n_songs == 'q':
        break
    album = make_album(a_name, a_title, n_songs)
    print(album)
