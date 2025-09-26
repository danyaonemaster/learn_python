from task_02_04_to_do_list import ToDoList


def test_to_do_list_class(capsys):
    list1 = ToDoList(["goha", "niga"])

    list1.add_task("Go to the school")

    assert list1.todo_list == ["goha", "niga", "Go to the school"]

    list1.show_tasks()

    res = capsys.readouterr().out.strip()

    assert res == "goha\nniga\nGo to the school"
