# 5.7 & 5.8 - Hello Admin & if No users
usernames = ['Rico', 'Admin', 'Liz', 'Batu', 'Chasel', 'Shawn']
if usernames:
    for username in usernames:
        if username == 'Admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('We need to find some users!')

# 5.9 - Checking Usernames
current_users = usernames[:]
new_users = ['rico', 'Kevin', 'liz', 'Joanne', 'Ailey', 'Jessica']
for new_user in new_users:
    if new_user in (user.lower() for user in current_users):
        print(f'Sorry, the username "{new_user}" has been taken.')
    else:
        print(f'The username "{new_user}" is available')

# 5.10 - Ordinal Numbers
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    elif num == 4:
        print('4th')
    elif num == 5:
        print('5th')
    elif num == 6:
        print('6th')
    elif num == 7:
        print('7th')
    elif num == 8:
        print('8th')
    elif num == 9:
        print('9th')        