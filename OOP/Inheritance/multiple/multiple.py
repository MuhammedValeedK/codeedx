class Teacher:
    def __init__(self,subject):
        self.subject = subject

class Researcher:
    def __init__(self, topic):
        self.topic = topic

class Professor(Teacher,Researcher):
    def __init__(self,name,subject,topic):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,topic)
        self.name = name

    def display_professor(self):
        print(f"My name is {self.name}, I teach {self.subject} and I research on {self.topic}")


prof1 = Professor( "Kahmas Khan","English","Environmental Studies")
prof1.display_professor()
     
        
        
        