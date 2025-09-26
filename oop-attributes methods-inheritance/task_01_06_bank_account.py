class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def withdraw(self, money):
        self.balance -= money

    def replenish(self, money):
        self.balance += money
