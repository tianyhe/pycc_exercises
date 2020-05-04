# 11.3 - Employee
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Create a employee instance and a custom raise amount for use in all test method."""
        self.employee = Employee('rico', 'he', 100_000_000)
        self.amount_raise = 100_000_000

    def test_give_default_raise(self):
        """Test that if a default raise is add to the annual salary properly."""
        self.employee.get_raise()
        self.assertEqual(self.employee.annual_salary, 100_005_000)

    def test_give_custom_raise(self):
        """Test that if a custom raise is add to the annual salary properly."""
        self.employee.get_raise(self.amount_raise)
        self.assertEqual(self.employee.annual_salary, 200_000_000)

if __name__ == "__main__":
    unittest.main()
