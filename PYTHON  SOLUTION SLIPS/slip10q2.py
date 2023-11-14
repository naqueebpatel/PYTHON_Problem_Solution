class Person():
    def __init(self):
        self.name=" "
        self.address=" "
    def Accept(self):
        self.name=input("ENTER PERSON NAME:::")
        self.address=input("ENTER PERSON ADDRESS:::")
    def Display(self):
        print("NAME:::",self.name)
        print("ADDRESS:::",self.address)
        
class Employee(Person):
    def __init__(self):
        self.sid=0
        self.sal=0
    def Accept(self):
        Person.Accept(self)
        self.sid=int(input("ENTER ID:::"))
        self.sal=int(input("ENTER SALARY:::"))
    def Display(self):
        Person.Display(self)
        print("STAFF ID:::",self.sid)
        print("SALARY:::",self.sal)
ObjList=[]
while True:
    obj=Employee()
    obj.Accept()
    ObjList.append(obj)
    ch=input("MORE DETAILS? Y/N")
    if ch=='N':
        break

for i in range(len(ObjList)):
    ObjList[i].Display()
