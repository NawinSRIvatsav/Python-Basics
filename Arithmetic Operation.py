x ="y"
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def power(a,b):
    return a**b

def main():
    a=float(input("Enter value of a:"))
    b=float(input("Enter value of b:"))

    print("""Enter an operation:
                1.ADDITION
                2.SUBTRACTION
                3.MULTIPLICATION
                4.DIVISION
                5.POWER """)

    option= input("Enter your choice:")

    if option=="1" or option=="add":
        print(add(a,b))
    elif option=="2" or option=="sub":
        print(sub(a,b))
    elif option=="3" or option=="mul":
        print(mul(a,b))
    elif option=="4" or option=="div":
        print(div(a,b))
    elif option=="5" or option=="power":
        print(power(a,b))    
    else:
        print("Invalid")

while(x=="y"):
    main()
    x =input("Do you want to continue(y/n):")
