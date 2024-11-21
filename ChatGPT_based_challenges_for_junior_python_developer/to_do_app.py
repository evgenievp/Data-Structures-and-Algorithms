import datetime


class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)
        return f"Task added at: {datetime.datetime.now()}"

    def complete_task(self, task_index: int):
        for idx in range(len(self.tasks)):
            if idx == task_index:
                task = self.tasks[idx]
                self.tasks.remove(idx)
                return f"Task {task} is completed at {datetime.datetime.now()}"
        return "Task Index out of bounds!"

    def show_tasks(self):
        result = ''
        for task in self.tasks:
            result += f"Task {task}\n"
        return result
