import math
while True:
    m =int(input("Enter a Length : "))
    n =int(input("Enter a Width : "))
    if m<=0 or n<=0:
        print("\nEnter positive numbers")
    else:
        def length ():
            for i in range(m):
                print("*",end="#")
        for i in range(n):
            print("")
            length()
        print("")
    print("")