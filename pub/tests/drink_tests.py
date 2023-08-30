import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("tennents", 5, 5)

    def test_name_of_drink(self):
        self.assertEqual("tennents", self.drink.name)

    def test_price_of_drink(self):
        self.assertEqual(5, self.drink.price)