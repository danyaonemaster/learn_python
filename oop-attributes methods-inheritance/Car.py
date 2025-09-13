class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f'{self.brand} {self.model} {self.year}')

    @classmethod
    def default_car(cls):
        return cls("Toyota", "Corolla", 2020)

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}"


