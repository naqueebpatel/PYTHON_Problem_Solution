class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        ar=3.14*self.radius*self.radius
        print("AREA:::",ar)
    def circum(self):
        cir=2*3.14*self.radius
        print("CIRCUMFERENCE:::",cir)
radius=int(input("ENTER RADIUS"))
obj=Circle(radius);
obj.area()
obj.circum()
