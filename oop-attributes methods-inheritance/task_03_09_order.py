class Order:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data):
        return cls(price=data["price"],
                   quantity=data["quantity"])
