# The equality operator (==) compares the values
# of both the operands and checks value equality

# Whereas the is operator checks whether both
# the operands refer to the same object

list1 = []
list2 = []
list3 = list1

if list1 == list2:
    print(True)
else:
    print(False)

if list1 is list2:
    print(True)
else:
    print(False)

if list1 is list3:
    print(True)
else:
    print(False)

list3 = list1 + list2
if list1 is list3:
    print(True)
else:
    print(False)


# To check the identity of object : id()
list1 = []
list2 = []
print(id(list1))
print(id(list2))
