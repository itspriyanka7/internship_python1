class School :
    school_name = "MET"

    def __init__(self,studentName):
        self.studentName = studentName
        School.school_name

    # Class Method
    @classmethod
    def classMethod(cls,updated_schoolName) :
        cls.school_name = updated_schoolName

    # Static Method
    @staticmethod
    def staticMethod() :
        print("Welcome to my College")

    def display(self) :
        print(self.studentName)
        print(School.school_name)

s1 = School("Priyanka")
s1.staticMethod()
s1.display()

School.classMethod("BKC")
s2 = School("Khushi")

s2.display()

