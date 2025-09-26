class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        self.price = self.price * 0.99

