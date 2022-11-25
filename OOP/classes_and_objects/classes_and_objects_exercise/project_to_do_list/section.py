from OOP.classes_and_objects.classes_and_objects_exercise.project_to_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        try:
            current_name = next(filter(lambda x: x.name == task_name, self.tasks))
            current_name.completed = True
            return f"Completed task {task_name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = []
        for i in self.tasks:
            current_state = i.completed
            if current_state is True:
                completed_tasks.append(i)

        for j in completed_tasks:
            for k in range(len(self.tasks)):
                if j == self.tasks[k]:
                    self.tasks.remove(j)
                    break

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = []
        result.append(f"Section {self.name}:")
        for i in self.tasks:
            result.append(f"{i.details()}")

        return "\n".join(result)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())




