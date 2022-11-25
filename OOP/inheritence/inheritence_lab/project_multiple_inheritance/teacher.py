from OOP.inheritence.inheritence_lab.project_multiple_inheritance.employee import Employee
from OOP.inheritence.inheritence_lab.project_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
