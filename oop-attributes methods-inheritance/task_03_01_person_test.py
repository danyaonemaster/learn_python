from task_03_01_person import Person


def test_person_class():

    goha = Person.from_birth_year("John", 1999)

    assert isinstance(goha, Person)
    assert goha.name == "John"
    assert goha.year == 1999