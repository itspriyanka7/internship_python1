class form:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} and My id is {self.id}")

class form1:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} and My id is {self.id}")    

Student1=form("Priyanka",1)
print(Student1.admission())

Student2=form1("Khushi",2)
print(Student2.admission())     