from telebot.types import User

class Session:
    def __init__(self, users):
        self.users = self.users = users if users is not None else []

    @classmethod
    def empty(cls):
        return cls(None)
