def addition(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

def subtraction(a,b):
    print(f"The difference of {a} and {b} is {a-b}")

def Multiplication(a,b):
    print(f'The product of {a} and {b} is {a*b}')

def Division(a,b):
    print(f"The division of {a} and {b} is {a//b}")

def Modulation(a,b):
    print(f"The Modulation of {a} and {b} is {a%b}")
choise=int(input(''' For addition press (1) \n For Subtraction press (2) \n For Multiplication press (3) \n For Division press (4) \n For Modulation press (5) \n Enter your choice: '''))
if choise>=1 and choise<=5:
    a=int(input("Enter the 1st number:"))
    b=int(input("Enter the 2nd number:"))
    if choise==1:
        addition(a,b)
    elif choise==2:
        subtraction(a,b)
    elif choise==3:
        Multiplication(a,b)
    elif choise==4:
        Division(a,b)
    elif(choise==5):
        Modulation(a,b)
else:
    print("Invalid Input by the user")