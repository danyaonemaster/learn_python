class Session:
    def __init__(self, users):
        self.users = users

    @classmethod
    def empty(cls):
        return cls(0)
