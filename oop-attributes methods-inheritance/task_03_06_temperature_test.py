from task_02_06_temperature import Temperature


def test_temperature_class():
    temperature = Temperature.from_fahrenheit(64.8)

    assert temperature.temperature == (64.8 - 32) * 5 / 9