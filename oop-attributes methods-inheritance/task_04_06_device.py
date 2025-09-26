class Device():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

class Phone(Device):
    def call(self, number):
        print(f"Calling {number} from {self.info()}")


class Tablet(Device):
    def draw(self):
        print(f"Drawing on {self.info()}")

