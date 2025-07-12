class Employee:
    """Class represenation for employee data"""
    on_duty = []
    def __init__(self, Name, id):
        self.Name = Name
        self.id = id
        self.tasks = []
        print(f"Employee created {self.Name} created with ID {self.id}")

    def add_work(self, task):
        self.tasks.append(task)

    def time_in(self):
        Employee.on_duty.append(self.Name)

    def time_out(self):
        Employee.on_duty.remove(self.Name)

class Recruiter(Employee):
    def __init__(self, Name, id):
        super().__init__(Name, id)
        print(f"{self.Name} is a {self.tasks}")
    def recruit(self):
        print("recruit")

class Developer(Employee):
    def __init__(self, Name, id):
        super().__init__(Name, id)
        print(f"{self.Name} is a {self.tasks}")
    def code(self):
        print("code")

developer1 = Developer("Richard","1234",)
developer1.code()
