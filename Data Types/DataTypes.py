# Assigning string to variable
# Strings are immutable

a = "This is String"
print(a)

# List in Python
# List are mutable

L = [1, "a", "List", "1+2"]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])

# A tuple is a sequence of immutable python object
# Tuples are generally faster than list

tup = (10, "b", "tuple", "45")
print(tup)
print(tup[1])

# iteration in python
i = 1
while i < 10:
    print(i, end=" ")
    i += 1
# Example 2
print()
s = "sarbodaya jena"
for i in s:
    print(i, end=" ")

# For Loop in List
print()
abc = [10, 20, 30, 40, 50, 60, 70]
for j in abc:
    print(j, end=" ")

# example for loop using range

for i in range(0, 10):
    print(i)

