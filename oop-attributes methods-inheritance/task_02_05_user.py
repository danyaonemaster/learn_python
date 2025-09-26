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
    def __init__(self, username):
        super().__init__(username, "admin")

    def permissions(self) -> str:
        return "Full access: can add, edit, delete users and settings"


class Guest(User):
    def __init__(self, username):
        super().__init__(username, "guest")

    def permissions(self) -> str:
        return "Read-only access: can view content but cannot modify"
