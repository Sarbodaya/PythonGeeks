# Accessing the tuple with indexing
Tuple1 = tuple("Geeks")
print("First element of Tuple : ")
print(Tuple1[1])

# Tuple Unpacking

Tuple1 = ("Sarbodaya Jena", "Indian Army", "Indian Navy", "Indian Air Force")
# This line unpack the values of tuple
a, b, c, d = Tuple1
print("Values after Unpacking : ")
print(a)
print(b)
print(c)
print(d)

# Concatenation of Two Tuples
Tuple1 = (1, 2, 3, 4, 5, 6)
Tuple2 = ("Hello", "Geeks", "Welcome")

Tuple3 = Tuple1 + Tuple2
print(Tuple3)

# Printing First Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("Tuple 2: ")
print(Tuple2)

# Printing Final Tuple
print("Final Tuple : ")
print(Tuple3)

# Slicing of a Tuple

Tuple1 = tuple("GEEKSFORGEEKS")

# Removing a first Element
print("Removal Of first element : ")
print(Tuple1[1:])

# Reversing a Table
print("Reversing a Table : ")
print(Tuple1[::-1])

# Printing elements of Range
print("Elements between Range 4-9 : ")
print(Tuple1[4:9])


# Deleting a Tupple
del Tuple1
print(Tuple1)
