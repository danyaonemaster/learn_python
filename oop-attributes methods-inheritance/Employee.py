class Employee:
    def __init__(self, position):
        self.position = position


class Manager(Employee):
    def __init__(self, position, time_size):
        super().__init__(position)
        self.time_size = time_size

    def info(self):
        return f"Employee {self.position} has {self.time_size} hours left."
