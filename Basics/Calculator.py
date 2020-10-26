def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

def Main():
    print("Please select operation - ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    op = int(input("Select operations form 1, 2, 3, 4 : "))
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    if(op == 1):
        print("Sum is : ",end=" ")
        add(a,b)
    elif(op == 2):
        print("Sub is :",end=" ")
        sub(a,b)
    elif (op == 3):
        print("Mul is :", end=" ")
        mul(a, b)
    elif (op == 4):
        print("Sub is :", end=" ")
        div(a, b)
    else:
        print("Invalid Input")

if __name__ == "__main__":
    Main()