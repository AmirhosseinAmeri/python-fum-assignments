class Date:
    def __init__(self,year1,month1,day1,year2,month2,day2):
        self.year1=year1
        self.month1=month1
        self.day1=day1
        self.year2=year2
        self.month2=month2
        self.day2=day2
        self.result={"year":self.year1,"month":self.month1,"day":self.day1}
    def Is_Date_Valid(self):
        if 0<=self.month1<=12 and 0<=self.month2<=12 and 0<=self.day1<=30 and 0<=self.day2<=30:
            return True
        else:
            return False
    def Get_Month_Name(self):
        month_list=["Farvardin","Ordibehesht","Khordad","Tir","Mordad","Shahrivar","Mehr","Aban","Azar","Day","Bahman","Esfand"]
        for i in range(12):
            if self.month1==i+1:
                self.month=month_list[i]  
    def show(self):
        self.result={"year":self.year1,"month":self.month,"day":self.day1}
        print(self.result["year"],"/",self.result["month"],"/",self.result["day"])
    def add(self):
        while True:
            self.year2=int(input("Enter a year:"))
            self.month2=int(input("Enter a month:"))
            self.day2=int(input("Enter a day:"))
            if Date.Is_Date_Valid(self)==True:
                day=self.day1+self.day2
                month=self.month1+self.month2
                year=self.year1+self.year2
                if day > 30:
                    day=day-30
                    month+=1
                while month>12:
                    month=month-12
                    year+=1
                self.day1=day
                self.month1=month
                self.year1=year
                break
            else:
                print("Please Enter a Valid Date")
    def sub(self):
        while True:
            self.year2=int(input("Enter a year:"))
            self.month2=int(input("Enter a month:"))
            self.day2=int(input("Enter a day:"))
            if Date.Is_Date_Valid(self)==True:
                day=self.day1-self.day2
                month=self.month1-self.month2
                year=self.year1-self.year2
                if day < 0:
                    month-=1
                    day=30+day
                if month < 0:
                    year-=1
                    month=12+month
                self.day1=day
                self.month1=month
                self.year1=year
                break
            else:
                print("Please Enter a Valid Date")
while True:
    exit=input("Do you with to continue(type e to exit):")
    if exit=="e":
        break
    r=Date(0,0,0,0,0,0)
    print("Date")
    while True:
        r.year1=int(input("Enter a year:"))
        r.month1=int(input("Enter a month:"))
        r.day1=int(input("Enter a day:"))
        if r.Is_Date_Valid()==True:
            while True:
                print("1_show")
                print("2_add")
                print("3_subtract")
                print("4_change the first date")
                op=input("Enter your Choice here :")
                if op=="1":
                    r.Get_Month_Name()
                    r.show()
                elif op=="2":
                    r.add()
                    r.Get_Month_Name()
                    r.show()
                elif op=="3":
                    r.sub()
                    r.Get_Month_Name()
                    r.show()
                elif op=="4":
                    break
                else :
                    print("Please pick a number from the menu")
        else:
            print("Please Enter a Valid Date")