class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

    def greet(self):
        print(F"Hello, {self.username}!")

    @classmethod
    def guest(cls):
        return cls(username="guest", role="guest")


class Admin(User):
    def __init__(self, username, role="admin"):
        super().__init__(username, role)

    def permission(self):
        print(F"Hello, {self.username}!")


class Guest(User):
    def __init__(self, username, role="guest"):
        super().__init__(username, role)

    def permission(self):
        print(F"Hello, {self.username}!")
