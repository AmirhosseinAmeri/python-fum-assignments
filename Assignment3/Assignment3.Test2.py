import random
while True:
    r=int(input("Enter How many numbers you want to randomly choose (Enter 0 to exit): "))
    if r==0:
        break
    s=int(input("Enter a number to start from : "))
    e=int(input("Enter a number to end with : "))
    if r <= e-s +1:
        numbers=[]
        pc_number = random.randint(s,e)
        numbers.append(pc_number)
        i=0
        while  len(numbers) < r:
            pc_number = random.randint(s,e)
            if pc_number not in numbers:
                numbers.append(pc_number)
        print (numbers)
    else:
        print("i can't pick",r,"numbers between",s,"_",e)
