class Vehicle():

    def drive(self):
        print("Driving")


class Car(Vehicle):

    def drive(self):
        print(f"Car is driving")


class Bike(Vehicle):

    def drive(self):
        print(f"Bike is riding")


def vehicle_class(capsys):
    c = Car()
    b = Bike()

    c.drive()
    b.drive()

    print(capsys.readouterr().out.strip())


