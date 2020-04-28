# 11.1 & 11.2 - City, Countrys & Populations
import unittest

from city_functions import get_formatted_string

class StringsTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_country(self):
        """Do value with 'city' and 'country' work?"""
        formatted_string = get_formatted_string('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do value with 'city, coutry, population' work?"""
        formatted_string = get_formatted_string('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
