from task_01_01_person import Person


def test_person_class():
    foo = Person("John", 18)

    print(foo.name)
    print(foo.age)

    assert foo.name == "John"
    assert foo.age == 18