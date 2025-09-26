class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, first_name, last_name, birth_year, grade):
        super().__init__(first_name, last_name)
        self.birth_year = birth_year
        self.grade = grade


class GraduateStudent(Student):
    def __init__(self, first_name, last_name, birth_year, ratings, grade = 12):
        super().__init__(first_name, last_name, birth_year, grade)
        self.ratings = ratings