print("List Iteration : ")
list1 = ['Sarbodaya', 'Jena', 'Army']
for i in list1:
    print(i)

print("Tuples Iteration : ")
tuple1 = ("Geeks", "For", "Geeks")
for i in tuple1:
    print(i)

print("String Iteration : ")
s = "geeks"
for i in s:
    print(i)

print("Dictionary Iteration : ")
d = dict()
d['xyz'] = 100
d['abc'] = 101
for i in d:
    print(f"{i} {d[i]}")

# Iterating by index of Sequence
list1 = ["Geeks", "For", "Geeks"]
for index in range(len(list1)):
    print(list1[index])
else:
    print("Inside Else Block")

# Nested Loops
print("Nested Loops : ")
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Loop Control Statements :
# Continue Statement: It returns the control to the beginning of the loop.
print("Continue Statement : ")
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print("Current Letter : ", letter)

# Break Statement :  It brings control out of the loop
print("Break Statement : ")
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        break
print("Current Letter : ", letter)

# Pass Statement : We use pass statement to write empty loops.
# Pass is also used for empty control statement, function and classes.

for letter in 'IndianAirForce':
    pass
print("Last Letter : ", letter)


