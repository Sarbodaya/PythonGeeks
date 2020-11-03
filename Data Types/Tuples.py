# Creating an Empty Table
Tuple1 = ()
print("Initial Empty Tuple : ")
print(Tuple1)

Tuple1 = ("Sarbodaya", "Jena")
print("Tuple with use of string : ")
print(Tuple1)

# Creating a Tuple With Help of List
List1 = [1, 2, 3, 4, 5, 6]
Tuple1 = tuple(List1)
print("Tuple using List : ")
print(Tuple1)

# Creating a tuple using built-in function
Tuple1 = tuple("Geeks")
print("Tuple with the use of function : ")
print(Tuple1)

# Creating a tuple with mixed data types
Tuple1 = (1, "Geeks", 12.34, "Welcome")
print("Tuple with mixed data types : ")
print(Tuple1)

# Creating a tuple with nested Tuples
Tuple1 = ("Sarbodaya", "Jena")
Tuple2 = ("Dreamed", "To", "Officer")
Tuple3 = (Tuple1, Tuple2)
print("Tuple with nested tuples : ")
print(Tuple3)

# Creating a tuple with repetition
Tuple1 = ("Service Before Self",)*3
print("Tuple with repetition : ")
print(Tuple1)

# Creating a tuple with use of loop
Tuple1 = ("Indian Army",)
n = 5
print("Tuple with loop : ")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)


