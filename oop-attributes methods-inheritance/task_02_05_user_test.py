from task_02_05_user import User


def test_user_class(capsys):
    user = User("John", "Doe")

    user.greet()

    res = capsys.readouterr().out.strip()

    assert res == "Hello, John!"
