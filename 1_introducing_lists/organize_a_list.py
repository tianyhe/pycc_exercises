# 3.8 - Seeing the World
locations = ['barcelona', 'montreux', 'amsterdam', 'los angles', 'cuba']
print('Original List:', locations)
    # alphabetical order without modifying the actual list
print('\nSorted Lists:', sorted(locations))
    # Show the original list
print('\nOriginal List:', locations)
    # reverse alphabetical order without modifying the actual list
print('\nTemp Reversed List:', sorted(locations, reverse=True))
    # Show the original list
print('\nOriginal List:', locations)
    # reverse() the list
locations.reverse()
print('\nPerm Reversed List:', locations)
    # reverse() the list again to change it back to original order
locations.reverse()
print('\nOriginal List:', locations)
    # sort() to permanently sort the list in alphabetical order
locations.sort()
print('\nNew List:', locations)
    # sort() to permanently sort the list in reverse alphabetical order
locations.sort(reverse=True)
print('\nNew Reversed List:', locations)

# 3.9 - Length of a List
print(f'\nHow many cities that i wanna visit? The answer is : " {len(locations)} ".')

