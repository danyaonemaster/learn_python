from task_02_10_account import Account


def test_account_class():
    bob = Account.create_with_bonus("Gorge")

    assert bob.balance != 0
