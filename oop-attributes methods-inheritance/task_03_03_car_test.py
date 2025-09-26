from task_01_02_car import Car


def test_car_constructor():
    car = Car.default_car()

    assert isinstance(car, Car)
    assert car.brand == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020

