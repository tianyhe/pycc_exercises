# 10.11 & 10.12  - Favoirte Number & Favorite Number Remembered
import json

def get_stored_favorite_number(file_path):
    """Get stored favorite number if avaliable."""
    try:
        with open(file_path) as fhand:
            favorite_number = json.load(fhand)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number(file_path):
    """Prompt for a new favorite number"""
    favorite_number = input("What is your favorite number?\n")
    with open(file_path, 'w') as fhand:
        json.dump(favorite_number, fhand)
    return favorite_number

def favorite_number(file_path):
    """Report the favorite number to the user"""
    favorite_number = get_stored_favorite_number(file_path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_favorite_number(file_path)
        print("Your favorite number has been stored.")

path = '8_files_and_exceptions/json/'
file_name = 'favorite_number.json'
file_path = path + file_name

favorite_number(file_path)
