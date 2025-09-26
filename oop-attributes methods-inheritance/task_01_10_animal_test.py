from task_01_10_animal import Animal


def test_animal_class(capsys):
    cat = Animal("Bob", "meow")
    cat.make_sound()

    res = capsys.readouterr().out.strip()

    assert res == "meow"


