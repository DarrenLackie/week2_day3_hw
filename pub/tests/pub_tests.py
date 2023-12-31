import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("lager", 5, 5)
        self.drink2 = Drink("cosmo", 10, 10)
        self.drink3 = Drink("gin and tonic", 7, 8)
        self.pub = Pub("big dirty bill's big dirty tavern", 100, [self.drink, self.drink2, self.drink3])
        self.customer = Customer("Darren", 150, 35)
        self.customer2 = Customer("Graham", 50, 17)

    def test_pub_has_same_name(self):
        self.assertEqual("big dirty bill's big dirty tavern", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer, self.drink)
        self.assertEqual(105, self.pub.till)

    # def test_pub_can_sell_drink(self):
    #     self.pub.add_drink(self.drink)
    #     self.pub.add_drink(self.drink2)
    #     self.pub.sell_drink(self.customer, self.drink)
    #     self.pub.sell_drink(self.customer2, self.drink)
    #     self.assertEqual(145, self.customer.wallet)
    #     self.assertEqual(105, self.pub.till)


    def test_check_customer_age(self):
        customer_age = self.pub.check_customer_age(self.customer2)
        if customer_age:
            self.pub.sell_drink(self.customer2, self.drink)
        self.assertEqual(100, self.pub.till)

    # def test_check_customer_drunkenness(self):
    #     customer_drunkenness = self.pub.check_customer_drunkenness(self.customer)
    #     if customer_drunkenness: