class Fraction:
    def __init__(self,numerator1,denominator1,numerator2,denominator2):
        self.numerator1=numerator1
        self.denominator1=denominator1
        self.numerator2=numerator2
        self.denominator2=denominator2
    def show(self):
        print(self.result[0],"/",self.result[1])
    def sum(self):
        self.result={}
        self.result[0]=(self.numerator1*self.denominator2)+(self.numerator2*self.denominator1)
        self.result[1]=(self.denominator1*self.denominator2)
    def sub(self):
        self.result={}
        self.result[0]=(self.numerator1*self.denominator2)-(self.numerator2*self.denominator1)
        self.result[1]=(self.denominator1*self.denominator2)
    def mult(self):
        self.result={}
        self.result[0]=(self.numerator1*self.numerator2)
        self.result[1]=(self.denominator1*self.denominator2)
    def dive(self):
        self.result={}
        self.result[0]=(self.numerator1*self.denominator2)
        self.result[1]=(self.numerator2*self.denominator1)
while True:
    Exit=input("do you wish to continue(type e to exit):")
    if Exit=="e":
        break
    r=Fraction(0,0,0,0)
    while True:
        print("First Fraction")
        r.numerator1=int(input("Enter a Numerator:"))
        r.denominator1=int(input("Enter a Denominator: "))
        if r.denominator1!=0:
            break
        else:
            print("Denominator can not be zero")
    while True:
        print("Second Fraction")
        r.numerator2=int(input("Enter a Numerator:"))
        r.denominator2=int(input("Enter a Denominator: "))
        if r.denominator2!=0:
            break
        else:
            print("Denominator can not be zero")
    while True:
        op=input("Enter Your Operation(+,-,*,/):")
        if op=="+":
            r.sum()
            r.show()
            break
        elif op=="-":
            r.sub()
            r.show()
            break
        elif op=="*":
            r.mult()
            r.show()
            break
        elif op=="/":
            r.dive()
            r.show()
            break
        else:
            print("Please pick from the defined oprations")