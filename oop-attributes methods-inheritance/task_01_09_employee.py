class Employee:
    def __init__(self, position):
        self.position = position


class Manager(Employee):
    def __init__(self, team_size):
        super().__init__("Manager")
        self.team_size = team_size

    def info(self):
        return f"Position: {self.position}, Team size: {self.team_size}"
