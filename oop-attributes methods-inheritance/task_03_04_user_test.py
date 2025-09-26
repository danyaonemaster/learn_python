from task_02_05_user_test import User


def test_user_class():
    guest = User.guest()

    assert guest.username == 'guest'
    assert guest.role == 'guest'