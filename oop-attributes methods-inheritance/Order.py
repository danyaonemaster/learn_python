class Order:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_order(cls, order):
        return cls(order.price, order.quantity)
