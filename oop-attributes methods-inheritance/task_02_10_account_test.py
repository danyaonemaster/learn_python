from task_02_10_account import Account


def test_account_class():
    account1 = Account("Roki", 1000)
    account2 = Account("Goha")

    account1.transfer_to(account2, 1000)

    assert account2.balance == 1000
    assert account1.balance == 0