import math
while True :
    num1 = float(input("Enter your Number : "))
    op = input("Enter Operation (Pick from + , - , * , / , radical , sin , cos , tan , cot , factorial , exit) : ")
    if op=="radical":
        re=math.sqrt(num1)
    if op=="sin":
        re=math.sin(num1)
    if op=="cos":
        re=math.cos(num1)
    if op=="tan":
        re=math.tan(num1)
    if op=="cot":
        re1=math.tan(num1)
        re=(1/num1)
    if op=="factorial" :
        num1=math.floor(num1)
        re=math.factorial(num1)
    if op == "+":
        num2 = float(input("Enter your Second Number : "))
        re=num1+num2
    if op == "-":
        num2 = float(input("Enter your Second Number : "))
        re=num1-num2
    if op == "*":
        num2 = float(input("Enter your Second Number : "))
        re=num1*num2
    if op == "/":
        num2 = float(input("Enter your Second Number : "))
        if num2==0:
            re = "you cannot divide by 0"
        else :
            re=num1/num2
    if op == "exit":
        break
    print("Your Result : ",re)