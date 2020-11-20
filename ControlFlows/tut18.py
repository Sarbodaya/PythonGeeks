print("Enter the number : ")
a = input()
print("Enter the second number : ")
b = input()
try:
    print("The sum of two numbers is : ", int(a) + int(b))
except Exception as e:
    print(e)
print("The line is Executed Successfully")
