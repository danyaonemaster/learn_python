from task_01_09_employee import *


def test_employee_class():
    goha = Manager(3)

    assert goha.info() == f"Position: {goha.position}, Team size: {goha.team_size}"