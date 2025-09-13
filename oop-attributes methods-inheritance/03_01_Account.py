class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}: Deposited {amount}. Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"{self.owner}: Insufficient funds.")
            return False
        self.balance -= amount
        print(f"{self.owner}: Withdrew {amount}. Balance: {self.balance}")
        return True

    def transfer_to(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            print(f"Transfer of {amount} from {self.owner} to {other_account.owner} completed.")
        else:
            print("Transfer failed.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

    @classmethod
    def create_with_bonus(cls, owner):
        return cls(owner, 100)
