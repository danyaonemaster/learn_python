from task_01_10_animal import *


def test_cat_class(capsys):
    bob = Cat(name="Bob")
    bob.meow()

    res = capsys.readouterr().out.strip()

    assert res == "meow"
