class Vehicle():
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"Car {self.brand} {self.model} is driving")


class Bike(Vehicle):
    def __init__(self, brand, type_bike):
        super().__init__(brand)
        self.type_bike = type_bike

    def drive(self):
        print(f"Bike {self.brand} {self.type_bike} is driving")
