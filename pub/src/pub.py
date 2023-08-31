class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks
        self.max_drunkenness_level = 20

    # def drink_count(self):
    #     return len(self.drinks)
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def remove_drink(self, drink):
        self.drinks.remove(drink)

    # def serve(self, customer, drink):
    #     if self.drinks.count(drink) == 0:
    #         return
    #     self.drinks.remove(drink)
    #     customer.buy_drink(drink)
    #     self.till += drink.price

    def sell_drink(self, input_customer, input_drink):
            if self.check_customer_age(input_customer):
                input_customer.buy_a_drink(input_drink)
                self.till += input_drink.price

    def check_customer_age(self, input_customer):
        if input_customer.age >= 18:
            return True
        else:
            return False
        
    def check_customer_drunkenness(self, input_customer):
        if input_customer.drunkenness > self.max_drunkenness_level:
            return True
        else:
            return False
        
    # def customer_old_enough(self, input_customer):
    #     return input_customer.age >= 18