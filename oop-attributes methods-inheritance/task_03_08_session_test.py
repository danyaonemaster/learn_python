from task_03_08_session import Session


def test_session():
    session = Session.empty()

    assert session.users == []