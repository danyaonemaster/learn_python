from task_01_06_bank_account import BankAccount
bank_account = BankAccount("Mercede", 1200)

def test_bank_account_withdraw():

    bank_account.withdraw(120)

    assert bank_account.balance == 1080

    bank_account.replenish(100)

    assert bank_account.balance == 1180

