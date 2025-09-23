class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_info(self):
        super().show_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

class manager(Employee):
    def __init__ (self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

manager1 = manager("John", 30, "E001", 50000, "Sales")
manager1.show_info()