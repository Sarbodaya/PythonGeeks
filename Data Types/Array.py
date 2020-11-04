# Creating Array : .array(data_type, value_list)
import array as arr

# Creating integer array
a = arr.array('i', [1, 2, 3])
print("The new array of integer type : ")
# Printing the original array
for i in range(0, 3):
    print(a[i], end=" ")

print()

# Creating an array of Float Type
b = arr.array('d', [1.2, 1.6, 8.9])
# Printing an original Array

print("The new created array is : ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
# Array of int type
c = arr.array('i', [1, 2, 3])
for i in range(0, 3):
    print(c[i], end=" ")

c.insert(1, 4)
print()
print("Array after insertion : ")
for i in (c):
    print(i, end=" ")

print()
# Array of float type :
d = arr.array('d', [1.4, 3.4, 5.7])
print("Before insertion of element : ")
for i in d:
    print(i, end=" ")
print()
print("After insertion of element : ")
d.insert(3, 67.8)
for i in (d):
    print(i, end=" ")

# Using append method
d.append(98.3)
print()
for i in d:
    print(i, end=" ")


# Popping an element : pop() and remove()
print()
e = arr.array('i', [1, 2, 3, 4, 5])
print("The popped element is : ", e.pop(0)) # from position
for i in e:
    print(i, end=" ")
print()
e.remove(5) # removes first occurrence of element 5
for i in e:
    print(i, end=" ")
print()
# Slicing
print("array slicing : ")
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = arr.array('i', z)
print(f[0:3])
print(f[2:6])

# Searching an element in an array : index()

print("the index of first occurrence of 2 in array : ", end="")
print(f.index(2))
mylist = [4, 5, 6, 7]
z.extend(mylist)
print('the index of first occurrence of 5 in array : ', end="")
print(f.index(4))

# Updating Elements in an array
# Simply reassign a new value to the desired location
for i in z:
    print(i, end=" ")
print()
z[0] = 100
# array After updating :
print("Array after updating : ")
for i in z:
    print(i, end=" ")


