"""A set of classes used to represent admin and admin's privileges"""
from users import Users

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
