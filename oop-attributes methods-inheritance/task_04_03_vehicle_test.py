from task_04_03_vehicle import *


def test_vehicle_class(capsys):
    c = Car()
    b = Bike()

    c.drive()
    b.drive()

    res = capsys.readouterr().out.strip()

    assert res == "Car is driving\nBike is riding"


