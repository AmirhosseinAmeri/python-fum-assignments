import math
while True:
    print ("\nax^2+ bx + c = 0\n")
    a=float(input("Enter a : "))
    b=float(input("Enter b : "))
    c=float(input("Enter c : "))
    d=((b*b)-(4*a*c))
    if d<0 :
        print ("\nsorry this equation can not be solved")
    else:
        rd=math.sqrt(d)
        x1=(-b + rd)/(2*a)
        x2=(-b - rd)/(2*a)
        print("\nThe solutions are:",x1,"and",x2)