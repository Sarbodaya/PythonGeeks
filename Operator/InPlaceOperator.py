# Python in its definition provides methods to perform inplace operations,
# i.e doing assignment and computation in a single statement using “operator” module.
# x+=y is equivalent to x = operator.iadd(x,y)

import operator

x = 10
y = 20
x = operator.iadd(x, y)
print("The value after adding and assigning : ", end="")
print(x)

x = "Geeks"
y = "ForGeeks"

x = operator.iconcat(x, y)
print("The string after concatenation : ", end="")
print(x)

x = operator.isub(2, 3)
print("The value after subtracting and assigning : ", end="")
print(x)

x = operator.imul(10, 100)
print("The value after multiplying and assigning : ", end="")
print(x)

x = operator.itruediv(100, 20)
print("The value after dividing and assigning : ", end="")
print(x)

x = operator.imod(10, 6)
print("The value after modulus and assigning : ", end="")
print(x)
