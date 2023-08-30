class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkenness = 0


    def buy_a_drink(self, input_drink):
        self.reduce_wallet(input_drink.price)
        self.drunkenness += input_drink.alcohol_level


    def reduce_wallet(self, input_amount):
        self.wallet -= input_amount