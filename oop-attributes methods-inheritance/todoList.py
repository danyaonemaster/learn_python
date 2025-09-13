class TodoList():
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def add_task(self, task):
        self.todo_list.append(task)

    def show_tasks(self):
        for task in self.todo_list:
            print(task)
