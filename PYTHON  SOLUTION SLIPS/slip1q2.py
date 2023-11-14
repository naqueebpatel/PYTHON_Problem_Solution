class InvalidDateException(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(self.value)
class Date():
    def __init__(self):
        self.dd=0
        self.mon=0
        self.yy=0
    def Accept(self):
        try:
            self.dd=int(input("ENTER DATE"))
            self.mon=int(input("ENTER MONTH"))
            self.yy=int(input("ENTER YEAR"))
            flag=0
            if mon>1 and mon<=12:
                    if mon==1 or mon==2 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12:
                        if mon==2:
                            if yr%4==0:
                                if dd>1 and dd<=29:
                                    flag=1
                                else:
                                    raise InvalidDateException("INVALID DATE!29 DAYS IN A LEAP YEAR")
                            else:
                                if dd>1 and dd<=28:
                                    flag=1
                                else:
                                    raise InvalidDateException("INVALID DATE!NOT A LEAP YEAR")
                        else:
                            if dd>1 and dd<=31:
                                flag=1
                            else:
                                raise InvalidDateException("INVALID DATE!MONTH CANNOT CONTAIN MORE THAN 31 DAYS")
                    elif mon==4 or mon==6 or mon==9 or mon==11:
                        if dd>1 and dd<=30:
                            flag=1
                        else:
                            raise InvalidDateException("INVALID DATE!MONTH CANNOT CONTAIN MORE THAN 31 DAYS")

            else:
                raise InvalidDateException("MONTH CANNOT BE GREATER THAN 12")
                    
        except InvalidDateException as e:
             print(e.value)
        if flag==1:
            Display()
            
    def Display(self):
        print("DATE IS VALID:::",dd,"/",mon,"/",yr)


obj=Date()
obj.Accept()
                            










