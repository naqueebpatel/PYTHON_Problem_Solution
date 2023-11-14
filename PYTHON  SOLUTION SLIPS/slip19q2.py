class Shape():
    def __init__(self):
        pass
    def Area(self):
        pass
    def Volume(self):
        pass

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length=length
    def Area(self):
        Shape.Area(self)
        area=self.length*self.length
        print("AREA OF SQUARE:::",area)
    def Volume(self):
        Shape.Volume(self)
        vol=self.length*self.length*self.length
        print("VOLUME OF SQUARE:::",vol)

class Circle(Shape):
    def __init__(self,radius):
        Shape.__init__(self)
        self.radius=radius
    def Area(self):
        Shape.Area(self)
        area=3.14*self.radius*self.radius
        print("AREA OF CIRCLE:::",area)
    def Volume(self):
        Shape.Volume(self)
        vol=2*3.14*self.radius
        print("VOLUME OF CIRCLE:::",vol)

length=int(input("ENTER LENGTH OF SQUARE"))
obj=Square(length)
obj.Area()
obj.Volume()

radius=int(input("ENTER THE RADIUS OF CIRCLE"))
obj=Circle(radius)
obj.Area()
obj.Volume()
