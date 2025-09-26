class Person:
    name: None
    year: None

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, year)
