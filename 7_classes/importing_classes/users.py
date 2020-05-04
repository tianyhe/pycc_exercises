"""A class that can be used to model a User's Profile."""

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
