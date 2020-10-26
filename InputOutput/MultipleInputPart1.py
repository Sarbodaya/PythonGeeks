# Generally, user use a split() method to split a Python string
# but one can use it in taking multiple input.

# taking two inputs at a time
x, y = input("Enter a two value : ").split()
print("Value of x : ", x)
print("Value of y : ", y)

# taking three times at a time
x, y, z = input("Enter a three value : ").split()
print("Total number os students : ", x)
print("Total no. of boys : ", y)
print("Total no. of girls : ", z)

# taking two inputs at a time
a, b = input("Enter two values : ").split()
print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("Enter a multiple value : ").split()))
print("List of students : ", x)



