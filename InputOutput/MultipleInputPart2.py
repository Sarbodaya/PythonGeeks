# Python program using how to take multiple inputs
# using List Comprehension

x, y = [int(x) for x in input("Enter two value : ").split()]
print("First number is : ", x)
print("Second number is : ", y)
print()

x, y, z = [int(x) for x in input("Enter three values : ").split()]
print("First number is : ", x)
print("Second number is : ", y)
print("Third  number is : ", z)
print()

x, y = [int(x) for x in input("Enter two values : ").split()]
print("First number is {} and second number is {}".format(x, y))
print()
x = [int(x) for x in input("Enter numbers : ").split()]
print("List of numbers : ", x)

# taking multiple values at a time separated by comma
z = [int(x) for x in input("Enter numbers : ").split(",")]
print("List of numbers : ", z)

