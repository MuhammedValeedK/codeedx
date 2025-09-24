#   manger & Developer are child classes inhert from parent class Employee

class employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_info(self):
        print(f"Name: {self.name}") 
        print(f"Employee ID: {self.employee_id}")    

class manager(employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

class developer(employee):
    def __init__(self,name, employee_id, programmimg_language):
        super().__init__(name, employee_id)
        self.programming_language = programmimg_language

    def show_info(self):
        super().show_info()
        print(f"Programming Language: {self.programming_language}")

