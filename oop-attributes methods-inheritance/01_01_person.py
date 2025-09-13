class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, age):
        return cls(name, age)

class Student(Person):
    def __init__(self, first_name, last_name, birth_year, grade):
        super().__init__(first_name, last_name)
        self.birth_year = birth_year
        self.grade = grade

class GraduateStudent(Student):
    def __init__(self, first_name, last_name, birth_year, ratings):
        super().__init__(first_name, last_name, birth_year, 12)
        self.ratings = ratings
