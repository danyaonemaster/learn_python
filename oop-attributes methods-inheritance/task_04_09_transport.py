class Transport:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

class Plane(Transport):
    def fly(self):
        print(f"{self.name} is flying in the sky!")

class Ship(Transport):
    def sail(self):
        print(f"{self.name} is sailing on the water!")