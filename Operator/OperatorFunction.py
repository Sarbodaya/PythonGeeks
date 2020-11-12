import operator
a = 4
b = 3
print("The addition of number is : ", end=" ")
print(operator.add(a, b))

print("Th difference of number is : ", end=" ")
print(operator.sub(a, b))

print("The product of number is : ", end=" ")
print(operator.mul(a, b))

print("The true division of number is : ", end=" ")
print(operator.truediv(a, b))

print("The floor division of number is : ", end=" ")
print(operator.floordiv(a, b))

print("The Exponential of number is : ", end=" ")
print(operator.pow(a, b))

print("The Modulus of number is : ", end=" ")
print(operator.mul(a, b))


if operator.lt(a, b):
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is greater than {b}")


if operator.le(a, b):
    print(f"{a} is less than or equal to {b}")
else:
    print(f"{a} is no the less than equal to {b}")


if operator.eq(a, b):
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is not equal to {b}")

if operator.gt(a, b):
    print("4 is greater than 3")
else:
    print("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if operator.ge(a, b):
    print("4 is greater than or equal to 3")
else:
    print("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if operator.ne(a, b):
    print("4 is not equal to 3")
else:
    print("4 is equal to 3")







