from functools import reduce

class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_mark(self):
        print(reduce(lambda x, y: x +y, self.grades)/len(self.grades))
