import random
pc_number = random.randint(1,20)
saved_numbers=[]
while True:
    user_number = int(input("Enter a number between 1_20: "))
    saved_numbers.append(user_number)
    if user_number < pc_number :
        print("Wrong , Pick a Higher number")
    if user_number > pc_number :
        print("Wrong , Pick a Lower number")
    if user_number == pc_number:
        print("You Won , Your numbers were :",saved_numbers)
        break