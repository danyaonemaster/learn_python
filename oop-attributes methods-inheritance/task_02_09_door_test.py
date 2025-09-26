from task_02_09_door import Door


def test_door_class():
    door = Door()

    door.open()
    assert door.is_open == True
    door.close()
    assert door.is_open == False

