class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task_list = [t for t in self.tasks if t.name == task_name]
        if task_list:
            task = task_list[0]
            task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [t for t in self.tasks if t.completed]
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        section_info = [f"Section {self.name}:"]
        tasks_info = [f"{t.details()}" for t in self.tasks]
        return "\n".join(section_info + tasks_info) + '\n'
