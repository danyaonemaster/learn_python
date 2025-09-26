from task_01_09_employee import Employee


def test_employee_class():
    goha = Employee("teacher")

    assert goha.position == "teacher"

    goha.position = "cleaner"

    assert goha.position == "cleaner"
