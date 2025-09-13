from functools import reduce

class ShoppingCart:
    def __init__(self, products, price):
        self.product_list = products
        self.product_price = price


    def total_price(self):
        return reduce(lambda x, y: x + y, self.product_price)


