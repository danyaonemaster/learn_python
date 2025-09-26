from task_01_08_laptop import Laptop

def test_laptop_class(capsys):

    laptop = Laptop("Asus", "DDR2", "ryzen 2400g")

    print(laptop)

    res = capsys.readouterr().out.strip()

    assert res == f"Laptop(Brand: {laptop.brand}, RAM: {laptop.ram}GB, CPU: {laptop.cpu})"

