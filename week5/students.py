class student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age 
        self.grade = grade
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, age: {self.age}, grade :{self.grade}")

    def update_grade(self,new_grade):
        self.grade = new_grade
        print (f"Grade of {self.name} updated to {new_grade}")

s1 = student ("Muhammed",45,30,"A+")
s2 = student ("Fathima",46,31,"A")
s1.display_info()
s2.display_info()
s2.update_grade("A+")
s2.display_info()


s3 = student("Valeed",35,30,"B")
s3.display_info()