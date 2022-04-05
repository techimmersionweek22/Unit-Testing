class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Client:
    all_clients = []
    
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
        self.purchases = []
        
    def purchase(self, product):
        if self.account_balance >= product.price:
            self.account_balance -= product.price
            self.purchases.append(product.name)
            