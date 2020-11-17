# Using Iterations In Python
# C style Approach
cars = ['Aston', 'Audi', 'McLaren']
i = 0
while i < len(cars):
    print(cars[i], end=" ")
    i += 1
print("\r")
# Accessing items using for-in loop

cars = ["Aston", "Audi", "McLaren"]
for x in cars:
    print(x, end=" ")
print("\r")

# Indexing using Range Functions
cars = ["Aston", "Audi", "McLaren"]
for i in range(len(cars)):
    print(cars[i], end=" ")
print("\r")

# Enumerate
# Enumerate is built-in python function that takes input as iterator, list etc and returns a
# tuple containing index and data at that index in the iterator sequence. For example,
# enumerate(cars), returns a iterator that will return (0, cars[0]),
# (1, cars[1]), (2, cars[2]), and so on.

cars = ["Aston", "Audi", "McLaren"]
for i, x in enumerate(cars):
    print(x, end=" ")

print("\r")

cars = ["Aston", "Audi", "McLaren"]
for x in enumerate(cars):
    print(x[0], x[1])
print("\r")

# We can also directly print returned value of enumerate() to see what it returns.
cars = ["Aston", "Audi", "McLaren"]
print(enumerate(cars))

# demonstrating the use of start in enumerate

cars = ["Aston", "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print(x[0], x[1])
