# 10.13 - Verify User
import json

def verify_username(file_path):
    """Verify if the current user is the user last used the program or not."""
    username = get_stored_username(file_path)
    ans = input(f"Is your username '{username}'? (Please enter 'y'/'n')\n")
    if ans == 'y':
        return username
    elif ans == 'n':
        return False

def get_stored_username(file_path):
    """Get stored username if avaliable."""
    try:
        with open(file_path) as fhand:
            username = json.load(fhand)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(file_path):
    """Prompt for a new username."""
    username = input("What's your name?\n")
    with open(file_path, 'w') as fhand:
        json.dump(username, fhand)
    return username

def greet_user(file_path):
    """Greet the user by name."""
    username = verify_username(file_path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(file_path)
        print(f"We'll remember you when you come back, {username}!")

path = '8_files_and_exceptions/json/'
file_name = 'username.json'
file_path = path + file_name

greet_user(file_path)
