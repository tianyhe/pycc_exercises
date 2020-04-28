"""A class that can be used to represent a restaurant."""

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
