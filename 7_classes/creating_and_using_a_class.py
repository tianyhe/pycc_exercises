# 9.1 - Restaurant
class Restaurant:
    """A Simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Present the information of the restaurant."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print('')

    def open_restaurant(self):
        """Stimulate openning a restaurant."""
        print(f"{self.restaurant_name} is now open.")

my_restaurant = Restaurant('He Dynasty', 'Chinese')
print('Name of the restaurant:', my_restaurant.restaurant_name)
print('Cuisine type:', my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9.2 - Three Restaurant 
your_restaurant = Restaurant('Liz Paradise', 'Korean')
your_restaurant.describe_restaurant()

his_restaurant = Restaurant('New Baby', 'French')
his_restaurant.describe_restaurant()

print('')

# 9.3 - Users
class Users:
    """A simple attempt to model User's Profile."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize first_name, last_name, age and gender attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Present a summary of the user's information."""
        print(f"User name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print('')

    def greet_user(self):
        """Personalized greeting to the user."""
        print(f"Hi {self.first_name.title()}, whats up?")
        print('')

my_profile = Users('rico', 'he', 23, 'Male')
your_profile = Users('liz', 'Zheng', 22, 'Female')
his_profile = Users('batu', 'onal', 24, 'Male')

my_profile.describe_user()
my_profile.greet_user()

your_profile.describe_user()
your_profile.greet_user()

his_profile.describe_user()
his_profile.greet_user()
