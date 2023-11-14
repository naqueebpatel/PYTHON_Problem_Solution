class Calculator():
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def Add(self):
        add=self.val1+self.val2
        print("ADDITION:::",add)
    def Sub(self):
        sub=self.val1-self.val2
        print("SUBTRACTION:::",sub)
    def Mul(self):
        mul=self.val1*self.val2
        print("MULTIPLICATION:::",mul)
    def Div(self):
        div=self.val1/self.val2
        print("DIVISION:::",div)

while True:
    print(":::SELECT OPERATION TO PERFROM:::")
    ch=int(input("1.ADDITION  2.SUBTRACTION   3.MULTIPLICATION   4.DIVISION   5.EXIT \n"))
    if ch>4:
        print("THANK YOU!!")
        break
    else:
        pass
    val1=int(input("ENTER VALUE 1:::"))
    val2=int(input("ENTER VALUE 2:::"))
    obj=Calculator(val1,val2)
    if ch==1:
        obj.Add()
    elif ch==2:
        obj.Sub()
    elif ch==3:
        obj.Mul()
    elif ch==4:
        obj.Div()
