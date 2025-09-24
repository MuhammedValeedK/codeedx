class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print (f"Name:{self.name}, Age:{self.age}")


class employee(person):
    def __init__(self, name, age, employee_id,mobile_number):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.mobile_number = mobile_number
    def display_employee(self):
        print(f"Name:{self.name}, Age:{self.age},Employee ID: {self.employee_id}, Mobile Number:{self.mobile_number}")

person1 = person()
person1 = employee("Ahmed", 45, "CE323", "85451524")

person1.display_employee()




