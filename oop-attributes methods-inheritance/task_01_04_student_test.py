from functools import reduce

from task_01_04_student import Student


def test_student_class(capsys):
    Gary = Student("John", [10, 9, 8, 2, 12])

    Gary.average_mark()

    res = float(capsys.readouterr().out.strip())

    average_mark = reduce(lambda x, y: x + y, Gary.grades) / len(Gary.grades)
    assert res == average_mark
