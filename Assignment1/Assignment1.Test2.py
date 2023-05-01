name = input("Enter name : ")
family = input("Enter family : ")
a = float (input ("Enter score a: "))
b = float (input ("Enter score b: "))
c = float (input ("Enter score c: "))
Average = (a+b+c)/3
if (Average<12) :
    print ("Status of",name , family, ": Fail")
else :
    if (12<=Average<17) :
        print ("Status of",name , family, ": Normal")
    else :
        if (17<=Average) :
            print ("Status of",name , family, ": Great")