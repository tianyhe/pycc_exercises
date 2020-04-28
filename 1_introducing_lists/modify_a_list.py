# 3.4 - Guest Lists
guests = ['Grandpa', 'Bill Gates', 'Mao Zedong']
for i in range(len(guests)):
    message = f'Good Evening {guests[i]}, please come by tonight at 6 pm sharpe for my dinner. Thank you!'
    print(message)
print('\n')

# 3.5 - Changing Guest List
print(f'Sadly, {guests[2]} can not make it to the dinner.')
guests = ['Grandpa', 'Bill Gates', 'Steve Jobs']
for i in range(len(guests)):
    message = f'Good Evening {guests[i]}, please come by tonight at 6 pm sharpe for my dinner. Thank you!'
    print(message)
print('\n')

# 3.6 - More Guests
print('Guys, i found a bigger dinner table')
guests.insert(0, 'Eminem')
guests.insert(2, 'Scarlett Johansson')
guests.append('Warren Buffett')
for i in range(len(guests)):
    message = f'Good Evening {guests[i]}, please come by tonight at 6 pm sharpe for my dinner. Thank you!'
    print(message)
print('\n')

# 3.7 - Shrinking Guest List
print('Sorry guys, table not gonna arrive in time. I can only invite two people')
guest = guests.pop()
print(f'Sorry {guest}, May be next time!')
guest = guests.pop()
print(f'Sorry {guest}, May be next time!')
guest = guests.pop()
print(f'Sorry {guest}, May be next time!')
guest = guests.pop()
print(f'Sorry {guest}, May be next time!')
print(f'Congrats {guests[0]}, please come by tonight as we planned')
print(f'Congrats {guests[1]}, please come by tonight as we planned')
del guests[:]
print(guests)