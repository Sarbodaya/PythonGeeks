# Creation of Set in Python
set1 = set()
print("Initial blank set : ")
print(set1)

# Creating a set using strings
set1 = set("GeeksForGeeks")
print("Set with the use of String : ")
print(set1)

del  set1

# Elements can be added to the set by using built - add() function

set1 = set()
print("Initial Blank Set : ")
print(set1)

# Adding element and tuple to Set

set1.add(10)
set1.add(12)
set1.add((6, 7))
print("Set after addition of three elements : ")
print(set1)

# Adding Elements to the sets using iterator
for i in range(1, 6):
    set1.add(i)

print("Set after addition of elements :  ")
print(set1)
del set1
# Using update method
# For addition of two or more elements

set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("Set After Addition of elements using Update : ")
print(set1)





