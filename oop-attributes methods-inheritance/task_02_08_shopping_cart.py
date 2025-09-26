from functools import reduce

class ShoppingCart:
    def __init__(self, product_price: dict[str, float] | None = None):
        self.product_price = product_price


    def total_price(self):
        return reduce(lambda x, y: x + y, self.product_price.values())


