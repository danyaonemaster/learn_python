class Laptop:
    def __init__(self, brand, ram, cpu):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        return f"Laptop(Brand: {self.brand}, RAM: {self.ram}GB, CPU: {self.cpu})"