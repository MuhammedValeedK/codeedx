#Single Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):  # Inheriting Person
    def __init__(self, name, age, employee_id, mobile):
        super().__init__(name, age)  # call Person constructor
        self.employee_id = employee_id
        self.mobile = mobile
    
    def display_employee(self):
        self.display()
        print(f"Employee ID: {self.employee_id}, Mobile: {self.mobile}")

emp1 = Employee ("Muhammed", 30, "1064", '8592949824')
emp1.display_employee()


# Multiple inheritance

class Driver:
    def __init__(self, license_type):
        self.license_type = license_type

    def drive(self):
        print(f"I drive vehicles with a {self.license_type} license.")


class Singer:
    def __init__(self, genre):
        self.genre = genre

    def sing(self):
        print(f"I sing {self.genre} songs.")


class Celebrity(Driver, Singer):  # Inherits both
    def __init__(self, name, license_type, genre):
        Driver.__init__(self, license_type)   # Initialize Driver
        Singer.__init__(self, genre)          # Initialize Singer
        self.name = name

    def showcase(self):
        print(f"{self.name} is a celebrity who drives with a {self.license_type} license "
              f"and sings {self.genre} songs.")

celeb1 = Celebrity("Daniel", "Heavy Vehicle", "Classical")
celeb1.showcase()



