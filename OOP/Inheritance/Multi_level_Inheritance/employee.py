# Manager class (inherits from) --> Employee class (inherits from) --> Person class 

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








#The Manager class inherits from the Employee class, which in turn inherits from Person. It's a special type of employee.
#class manager(Employee):: This line defines the Manager class, inheriting from Employee.
#def __init__(self, name, age, employee_id, salary, department):: The constructor for Manager takes all the arguments of Employee plus a new one: department.
#super().__init__(name, age, employee_id, salary): This calls the __init__ method of the parent class (Employee). It correctly initializes all the attributes from Employee (and by extension, from Person).
#self.department = department: This adds the department attribute, specific to managers.