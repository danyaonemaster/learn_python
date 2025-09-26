class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:

            self.balance += amount

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount
        return True

    def transfer_to(self, other_account, amount):
        if self.withdraw(amount):

            other_account.deposit(amount)

        else:
            print("Transfer failed.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

    @classmethod
    def create_with_bonus(cls, owner):
        return cls(owner, 100)
