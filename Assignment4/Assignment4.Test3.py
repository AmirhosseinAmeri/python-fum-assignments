print("\nFibonacci Printer\n")
while True:
    n=int(input("Enter a Number : "))
    print("")
    if n <= 0:
        print("Enter a positive number")
    else:
        a=0
        b=1
        for i in range(n):
            print(a,end=",")
            c=a+b
            a=b
            b=c
    print("")
    print("")