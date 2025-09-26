class ToDoList():
    def __init__(self, todo_list = None):
        self.todo_list = todo_list if todo_list is not None else []

    def add_task(self, task):
        self.todo_list.append(task)

    def show_tasks(self):
        string = "\n".join(self.todo_list) if self.todo_list else "list is empty"
        print(string)

