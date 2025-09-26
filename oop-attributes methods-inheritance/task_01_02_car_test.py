from task_01_02_car import Car


def test_car_class(capsys):
    car = Car("Mercede", "CLK-3000", 2015)

    car.info()

    res = capsys.readouterr().out.strip()

    assert res == "Mercede, CLK-3000, 2015"
