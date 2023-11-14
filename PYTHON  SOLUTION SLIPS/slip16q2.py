class Employee():
    def __init__(self):
        self.name=" "
        self.address=" "
    def Accept(self):
        self.name=input("ENTER NAME:::")
        self.address=input("ENTER ADDRESS:::")
    def Display(self):
        print("EMPLOYYE NAME:::",self.name)
        print("EMPLOYEE ADDRESS:::",self.address)

class Staff(Employee):
    def __init__(self):
        self.sid=0
        self.sal=0.0
    def Accept(self):
        Employee.Accept(self)
        self.sid=int(input("ENTER STAFF ID:::"))
        self.sal=int(input("ENTER SALARY:::"))
    def Display(self):
        Employee.Display(self)
        print("STAFF ID:::",self.sid)
        print("SALARY:::",self.sal)

ObjList=[]
while True:
    obj=Staff()
    obj.Accept()
    ObjList.append(obj)
    ch=input("MORE DETAILS? Y/N")
    if ch=='N':
        break
for i in range(len(ObjList)):
    ObjList[i].Display()
     
