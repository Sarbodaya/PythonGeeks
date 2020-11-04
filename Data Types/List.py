l = [10, 20, 30, 40]

print(l)
print(l[0])
print(l[1])
# This represents the last element
print(l[-1])
# Represents second last element
print(l[-2])

# Append()
l.append(50)
print(l)

# Insert()
l.insert(1, 15)
print(l)

print(15 in l)

# Count
print(l.count(40))

# Index
print(l.index(30))

# Index method with extra arguments :
# 1. Start index : - inclusive
# 2. End index ; - Exclusive

print(l.index(30, 4, 7))
