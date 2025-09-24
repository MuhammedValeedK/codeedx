#   Manager, Developer & Intern are child classes inhert from parent class Employee

class Employee :
    def __init__(self,name, id, basic_salary):
        self.name = name
        self.id = id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Basic Salary: {self.basic_salary}")

class Manager(Employee):
    def __init__ (self,name,id,basic_salary,bonus):
        super().__init__(name,id,basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus
    
    def show_info(self):
        super().show_info()
        print(f"Bonus: {self.bonus}")
        print(f"Total Pay:{self.calculate_salary()}")
        print("------------")

class Developer(Employee):
    def __init__(self,name,id,basic_salary,allowance):
        super().__init__(name,id,basic_salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.basic_salary + self.allowance
    
    def show_info(self):
        super().show_info()
        print(f"Allowance:{self.allowance}")
        print(f"Total_pay:{self.calculate_salary()}")
        print("------------")

class Intern(Employee):
    def __init__(self, name, id, stipend):
        super().__init__(name, id, 0) 
        self.stipend = stipend

    def show_info(self):
        super().show_info()
        print(f"Stipend: {self.stipend}")
        print("------------")
    



manager1 = Manager("Ameer", "CE3231", 25000, 10000)
manager1.show_info()

developer1 = Developer("Valeed", "CE3432", 22000, 7000 )
developer1 = developer1.show_info()

intern1 = Intern("Farhan", "IN3242", 10000)
intern1.show_info()