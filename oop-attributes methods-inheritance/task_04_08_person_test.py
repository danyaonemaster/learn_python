from task_01_01_person import *
import inspect


def test_person():
    params1 = inspect.signature(Person.__init__).parameters

    assert len(params1) -1 == 2

    params2 = inspect.signature(Student.__init__).parameters

    assert len(params2) -1 == 4

    params3 = inspect.signature(GraduateStudent.__init__).parameters

    assert len(params3)  == 5