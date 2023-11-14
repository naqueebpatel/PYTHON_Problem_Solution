class Student():
    def __init__(self):
        self.rno=0
        self.name=" "
        self.age=0
        self.gender=" "
    def StudAccept(self):
        self.rno=int(input("ENTER ROLL NO:::"))
        self.name=input("ENTER NAME:::")
        self.age=int(input("ENTER AGE:::"))
        self.gender=input("ENTER GENDER:::")
    def StudDisplay(self):
        print("ROLL NO:::",self.rno)
        print("NAME:::",self.name)
        print("AGE:::",self.age)
        print("GENDER:::",self.gender)

class Test(Student):
    def __init__(self):
        self.m1=0
        self.m2=0
        self.m3=0
        self.total=0
    def TestAccept(self):
        Student.StudAccept(self)
        self.m1=int(input("ENTER MARKS 1:::"))
        self.m2=int(input("ENTER MARKS 2:::"))
        self.m3=int(input("ENTER MARKS 3:::"))
        self.total=self.m1+self.m2+self.m3
    def TestDisplay(self):
        Student.StudDisplay(self)
        print("MARKS 1:::",self.m1)
        print("MARKS 2:::",self.m2)
        print("MARKS 3:::",self.m3)
        print("TOTAL MARKS :::",self.total)

obj=Test()
obj.TestAccept()
obj.TestDisplay()

        
