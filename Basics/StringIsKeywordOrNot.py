# Python code to demonstrate working of iskeyword()
import keyword

key = ["while", "sarbodaya", "for", "global", "nonlocal", "lambda", "Tanishq", "Rahul", "def", "import"]

for i in range(len(key)):
    if keyword.iskeyword(key[i]):
        print(key[i], " is a keyword")
    else:
        print(key[i], " is not a keyword")

# How to print list of all keywords?

print("List of all keywords in python : ")
print(keyword.kwlist)

a = 5
print("Value of a variable : " + str(a))


# One liner if-else instead of Conditional Operator (?:) in Python

b = 1 if 20 > 10 else 0
print("The value of b " + str(b))
# Print without newline in Python 3.x
print("geeksforgeeks",end=" ")
print("Hello Geeks")

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i],end=" ")

