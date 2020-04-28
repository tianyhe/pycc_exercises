# 9.6 - Ice Cream Stand
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


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream Stand'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['watermelon', 'strawberry', 'vanilla', 'banana', 'lemon']

    def describe_flavors(self):
        """Display all the flavors that the ice cream stand provide."""
        print(f"The Ice Cream Stand offer the following flavors: {self.flavors}\n")

my_stand = IceCreamStand('Wonderland')
my_stand.describe_restaurant()
my_stand.describe_flavors()

# 9.7 & 9.8 - Admin & Privileges
class Users:
    """A simple attempt to model User's Profile"""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize first_name, last_name, age and gender attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0    

    def describe_user(self):
        """Present a summary of the user's information"""
        print(f"User name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Login Attempts: {self.login_attempts}")
        print('')

    def greet_user(self):
        """Personalized greeting to the user"""
        print(f"Hi {self.first_name.title()}, whats up?")
        print('')

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0


class Privileges():
    """A simple attempt to model the privileges which an admin have"""

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user', 'can modify post', 'can hide post']):
        """Initialize the privileges' attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """List all the privileges that an administrator have"""
        print(f"Privileges: {self.privileges}\n")


class Admin(Users):
    """Represent aspects of a user, specific to administrator"""

    def __init__(self, first_name, last_name, age, gender):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an administrator
        """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

admin_profile = Admin('tianyao', 'he', 23, 'Male')
admin_profile.describe_user()
admin_profile.privileges.show_privileges()