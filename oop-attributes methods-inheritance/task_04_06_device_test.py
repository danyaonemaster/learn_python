from task_04_06_device import *


def test_phone_class(capsys):
    dev = Phone("Apple", "14 Pro")
    dev.call(103)

    res = capsys.readouterr().out.strip()

    assert res == "Calling 103 from Apple 14 Pro"

def test_table_class(capsys):
    dev = Tablet("Sosung", "S21")
    dev.draw()

    res = capsys.readouterr().out.strip()

    assert res == "Drawing on Sosung S21"