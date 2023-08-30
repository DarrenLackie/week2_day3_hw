class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def sell_drink(self, input_customer, input_drink):
        if self.check_customer_age(input_customer):
            input_customer.buy_a_drink(input_drink)
            self.till += input_drink.price


    def check_customer_age(self, input_customer):
        if input_customer.age >= 18:
            return True
        else:
            return False
