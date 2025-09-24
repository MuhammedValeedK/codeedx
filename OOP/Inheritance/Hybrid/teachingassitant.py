
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def display_info(self):
        print (f"Name:{self.name}, Age:{self.age}")


class Student(Person):
    def __init__(self, name,age,roll_no,course):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.course = course
    
    def display_student(self):
        super().display_info()
        print(f"Roll no: {self.roll_no}, Course: {self.course}")
        


class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        Person.__init__(self,name, age)
        self.employee_id = employee_id
        self.subject = subject

    def display_teacher(self):
        super().display_info()
        print(f"Employee_id: {self.employee_id}, Subject: {self.subject}")
        

class TeachingAssitant(Teacher,Student):
    def __init__(self,name,age, roll_no, course, employee_id,subject):
        Person.__init__(self,name,age)
        Student.__init__(self,name,age,roll_no,course)
        Teacher.__init__(self,name,age,employee_id,subject)
    
    def display_all(self):
        print("Teaching Assitant Details")
        Student.display_student(self)
        Teacher.display_teacher(self)   




assistant1 = TeachingAssitant("Muhammed",34,254,"MCA", "CE956", "Python")
assistant1.display_all() 