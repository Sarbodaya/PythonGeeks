# Case 1 : Immutable Targets
# Python code to demonstrate difference between
# Inplace and Normal operators in Immutable Targets

# importing operator to handle operator operations
# Case 1 : Immutable Targets.
# In Immutable targets, such as numbers, strings and tuples. Inplace operator behave
# same as normal operators, i.e only assignment takes place,
# no modification is taken place in the passed arguments.

import operator
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
z = operator.add(a, b)

# using iadd() to add the arguments passed
p = operator.iadd(x, y)

print("Value after adding using normal operator : ", end=" ")
print(z)

print("Value after adding using Inplace operator : ", end=" ")
print(p)

# printing value of first argument
# value is unchanged
print("Value of first argument using normal operator : ", end="")
print(a)

# printing value of first argument
# value is unchanged
print("Value of first argument using Inplace operator : ", end="")
print(x)


# Case 2 : Mutable Targets
# The behaviour of Inplace operators in mutable targets, such
# as list and dictionaries, is different from normal operators.
# The updation and assignment both are carried out in case of mutable targets.
print("Case 2 : Mutable Targets")
list1 = [1, 2, 4, 5]

# Using add() to add the arguments passed
z = operator.add(list1, [11, 12, 13])

print("Value after adding using normal operator : ", end="")
print(z)

print("Value of first argument using normal operator : ", end="")
print(list1)

p = operator.iadd(list1, [11, 12, 13])
print("Value after adding using inplace operator : ", end="")
print(p)

print("Value of first arguments using inplace operator : ", end="")
print(list1)



