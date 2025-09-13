from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        current_year = datetime.now().year
        age = current_year - year
        return cls(name, age)

    def __str__(self):
        return f"{self.name}, {self.age} years old"


