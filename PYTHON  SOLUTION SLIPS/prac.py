class Student():
    def __init__(self):
        self.age=int(input("ENTER AGE"))
    def __gt__(self,o):
        return (self.age>o.age)
obj1=Student()
obj2=Student()
if obj1>obj2:
    print("OBJECT 1 IS GREATER")
else:
    print("OBJECT 2 IS GREATER")
    
