# Dictionary in Python is unordered collection of data values
# used to store data values like a map
# Note :- Keys in Dict does not allow polymorphism

# Creating dict with integer key
Dict = {1: 'Geeks', 2: "For", 3: 'Geeks'}
print("Creating Dict with integer key : ")
print(Dict)

# Creating a Dict with mixed Keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4, 5]}
print('Dictionary used with different keys : ')
print(Dict)

del Dict
# Creating a Empty Dictionary
# Using built-in function
Dict = {}
print("Empty Dictionary : ")
print(Dict)

Dict = dict({1: "Hello", 2: "Sarbodaya", 3: "Jena"})
print("Dictionary with the use of dict() : ")
print(Dict)

Dict = dict([(1, "Geeks"), (2, "For",), (3, "Geeks")])
print("Dictionary with each item as pair : ")
print(Dict)


# Creating a Nested Dict
Dict = {1: "Sarbodaya", 2: "Jena", 3: {'A': "Welcome", 'B': 'To', 'C': 'Geeks'}}
print(Dict)

del Dict

# Creating a Empty Dictionary
Dict = {}
print("Empty Dict : ")
print(Dict)

Dict[0] = 'Geeks'
Dict[1] = 'For'
Dict[2] = 'Geeks'

print("Dict after adding three elements : ")
print(Dict)

# Adding set of values to single keys :
Dict['Value Set'] = 2, 3, 4
print("Dictionary After adding three elements : ")
print(Dict)

# Updating Existing Key Value
Dict[2] = 'Indian Air Force'
print("Updating a Existing Value : ")
print(Dict)

# Adding a Nested Key Value Pair
Dict[4] = {1: 'Life', 2: 'For', 3: 'GeeksForGeeks'}
print("Adding Nested Key Value Pair : ")
print(Dict)

del Dict
# Accessing Elements from Dictionary

Dict = {0: {'Geeks'}, 'Name': {'Sarbodaya'}, 3: {'Jena'}}
print("Accessing elements using key : ")
print(Dict['Name'])

# Accessing element using get() method

print("Accessing element using get() method : ")
print(Dict.get(3))

del Dict

# Accessing element of nested Dictionary

Dict = {1: {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 2: {1: 'Indian Army', 2: 'Indian Navy', 3: 'Indian Air Force'}}
print(Dict[1][2])
print(Dict[2][2])
print(Dict[1][3])


# Del Keyword
del Dict[1]
print('Deleting a specific key : ')
print(Dict)

del Dict[2][3]
print("Deleting a key From Nested Dictionary : ")
print(Dict)

del Dict

# Deleting a key
# using pop() method

Dict = {1: "Sarbodaya", 2: "Jena", 3: "Indian Army Officer"}
a = Dict.pop(1)
print("Dictionary after deletion : " + str(Dict))
print("Value associated to poped key : " + str(a))


# Deleting an entire Dict
Dict.clear()
print("Deleting a entire Dictionary : ")
print(Dict)

# str(Dic)

D1 = {'Name': 'Sarbodaya', 'Age': 19}
print("The Constituents Of Dict as string : ", str(D1))

# Using items() to display Dict as Lis
print("The Constituents of Dict as List : ", D1.items())

# len() : It returns count of key entitles of the dictionary Element
print("The Size of dict : ")
str =len(D1)

Dict3 = D1.copy()
print("The new copied Dictionary is : ")
print(Dict3)

# fromkeys(seq, value) : Used to Declare a new Dict from the sequence mentioned in its arguments

dic1 = {'Name' : 'Sarbodya', 'Age' : '20'}
dic2 = {'Id': 11804093}

dic1.update(dic2)
print("Updated Dictionary : ")
print(str(dic1))

seq = ('Name', 'Age', 'Id')

dict = dict.fromkeys(seq, 5)
print("The new dictionary values are : ")
print(str(dict))














