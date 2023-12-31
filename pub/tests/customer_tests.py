import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from tests.pub_tests import TestPub


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Darren", 150, 35)
        self.drink = Drink("tennents", 5, 5)

    def test_customer_has_name(self):
        self.assertEqual("Darren", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(150, self.customer.wallet)    

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(140, self.customer.wallet)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.drink)
        self.assertEqual(145, self.customer.wallet)

    def test_alcohol_level(self):
        self.customer.buy_a_drink(self.drink)
        self.assertEqual(5, self.customer.drunkenness)

    