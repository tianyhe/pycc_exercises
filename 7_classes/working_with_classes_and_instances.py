# 9.4 - Number Served
class Restaurant:
    """A Simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Present the information of the restaurant."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number of served customers: {self.number_served}")
        print('')    

    def open_restaurant(self):
        """Stimulate openning a restaurant."""
        print(f"{self.restaurant_name} is now open.")
    
    def set_number_served(self, number_served_customers):
        """Set the number_served to the given value."""
        if number_served_customers >= self.number_served:
            self.number_served = number_served_customers
        else:
            print(f"({number_served_customers}) is an Invalid Input")    

    def increment_number_served(self, number_new_customers):
        """Add the given amount of new served customers to the number_served."""
        if number_new_customers > 0:
            self.number_served += number_new_customers
        else:
            print(f"({number_new_customers}) is an Invalid Input")

my_restaurant = Restaurant('He Dynasty', 'Chinese')
my_restaurant.describe_restaurant()
print("----Modifying the number_served's Value Directly---")
my_restaurant.number_served = 10
my_restaurant.describe_restaurant()
print("----Modifying the number_served's Value Through a Method---")
my_restaurant.set_number_served(20)
my_restaurant.set_number_served(15)
my_restaurant.describe_restaurant()
print("----Incrementing the number_served's Value Through a Method---")
my_restaurant.increment_number_served(10)
my_restaurant.describe_restaurant()

print('')

# 9.5 - Login Attempts
class Users:
    """A simple attempt to model User's Profile."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize first_name, last_name, age and gender attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0    

    def describe_user(self):
        """Present a summary of the user's information."""
        print(f"User name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Login Attempts: {self.login_attempts}")
        print('')

    def greet_user(self):
        """Personalized greeting to the user."""
        print(f"Hi {self.first_name.title()}, whats up?")
        print('')

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

my_profile = Users('rico', 'he', 23, 'Male')
my_profile.describe_user()

print("---Increment the Login Attempts by 1---")
my_profile.increment_login_attempts()
print(f"Login Attempts: {my_profile.login_attempts}")
my_profile.increment_login_attempts()
print(f"Login Attempts: {my_profile.login_attempts}")
my_profile.increment_login_attempts()
print(f"Login Attempts: {my_profile.login_attempts}\n")

print("---Current Status of the User---")
my_profile.describe_user()

print(f"---Reset the Login Attempts to 0---")
my_profile.reset_login_attempts()
my_profile.describe_user()


