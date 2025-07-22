class Form1:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def admission(self):
        print(self.name)
        print(self.id)

class Form2(Form1):
    def __init__(self, name, id ,m_no):
        super().__init__(name,id)
        self.m_no=m_no

        def admission(self):
            print(self.m_no)

class Form3(Form1):
    pass
F2=Form3("Khushi",2)
print(F2.name)
print(F2.id)



F1=Form2("Priyanka",1,123456789)
print(F1.name)
print(F1.id)
print(F1.m_no)
