from task_02_06_temperature import Temperature


def test_temperature_class():
    temp = Temperature(18)

    temp.to_fahrenheit()

    assert temp.temperature == 64.4
