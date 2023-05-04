import random
while True:
    input1=input ("Press Enter to roll a dice ...")
    if input1=="":
        num=random.randint(1,6)
        if num != 6:
            print ("You rolled a :",num)
            break
        else :
            print ("You rolled a :",num,", You can roll again")