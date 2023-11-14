class Circle():
    def __init__(self):
        self.radius=int(input("ENTER RADIUS OF CIRCLE"))
        self.area=0
    def Area(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def __sub__(self,obj):
        return self.radius-obj.radius
obj1=Circle()
obj2=Circle()
print("AREA OF CIRCLE 1:::",obj1.Area())
print("AREA OF CIRCLE 2:::",obj2.Area())
print("SUBTRACTION OF RADIUS IS:::",obj1-obj2)
