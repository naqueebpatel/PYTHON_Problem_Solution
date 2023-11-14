class Country():
    def __init__(self):
        self.country=" "
        self.nationality=" "
    def Accept(self):
        self.country=input("ENTER COUNTRY:::")
        self.nationality=input("ENTER NATIONALITY:::")
    def Display(self):
        print("COUNTRY:::",self.country)
        print("NATIONALITY:::",self.nationality)

class State(Country):
    def __init__(self):
        self.state=" "
    def Accept(self):
        Country.Accept(self)
        self.state=input("ENTER STATE:::")
    def Display(self):
        Country.Display(self)
        print("STATE:::",self.state)
obj=State()
obj.Accept()
obj.Display()
        
