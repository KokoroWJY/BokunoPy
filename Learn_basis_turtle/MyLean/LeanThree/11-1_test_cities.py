import unittest
from city_function import city_country


class test_city_country(unittest.TestCase):

    def test_cityandcountry(self):
        test_city = city_country('santiago', 'chile')
        self.assertEqual(test_city, 'Santiago, Chile - population 0.')

    def test_city_country_population(self):
        test_city = city_country('santiago', 'chile', '50000')
        self.assertEqual(test_city, "Santiago, Chile - population 50000.")


unittest.main()