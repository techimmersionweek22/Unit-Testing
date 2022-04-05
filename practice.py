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
        Client.all_clients.append(name)
        
    def purchase(self, product):
        if self.account_balance >= product.price:
            self.account_balance -= product.price
            self.purchases.append(product.name)
            
    # def change_name(self, new_name):
    #     name_idx = Client.all_clients.index(self.name)
    #     Client.all_clients[name_idx] = new_name
    #     self.name = new_name
            