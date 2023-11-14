class Employee():
    id=0
    name=" "
    salary=0
    dept=" "
    def Accept(self):
        self.id=int(input("ENTER ID"))
        self.name=input("ENTER NAME")
        self.salary=int(input("ENTER SALARY"))
        self.dept=input("ENTER DEPATMENT")
    def Display(self):
        print("ID:::",self.id)
        print("NAME:::",self.name)
        print("SALARY:::",self.salary)
        print("DEPARTMENT:::",self.dept)
        
class Manager(Employee):
    #bonus=0
    #total=0
    def __init__(self):
        self.bonus=0
        self.total=0
    def MangAccept(self):
        Employee.Accept(self)
        self.bonus=int(input("ENTER BONUS"))
        self.total=self.salary+self.bonus
        
    def MangDisplay(self):
        Employee.Display(self)
        print("BONUS:::",self.bonus)
        print("TOTAL:::",self.total)

ObjectList=[]
while(True):
    obj=Manager()
    obj.MangAccept()
    ObjectList.append(obj)
    ch=input("MORE DETAILS Y/N")
    if ch=='N':
        break

max=0
m=0
for i in range(len(ObjectList)):
  ObjectList[i].MangDisplay()
  if(ObjectList[i].total>max):
      max=ObjectList[i].total
      m=i
      
print("HIGHEST SALARY DETAILS")
print(ObjectList[m].MangDisplay())
            
        
