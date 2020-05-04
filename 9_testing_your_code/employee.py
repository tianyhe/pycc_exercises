# 11.3 - Employee
class Employee():
    """A class to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize attributes to represent an employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def get_raise(self, amount_raise=5000):
        """Raise employee annual salary with a default value of 5k."""
        self.annual_salary += amount_raise
