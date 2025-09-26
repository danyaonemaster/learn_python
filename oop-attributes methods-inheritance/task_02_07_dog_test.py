from task_02_07_dog import Dog

def test_dog_class(capsys):
    dog = Dog("soda")
    dog.bark()

    res = capsys.readouterr().out.strip()

    assert res == "Woof-woof"