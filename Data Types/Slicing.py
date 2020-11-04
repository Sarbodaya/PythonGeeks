
# Slicing (List, Tuple, String)
# l[start : stop ; step] Stop is not included (We Stop before step)

l = [10, 20, 30, 40, 50]
print("String Slicing")
print(l[0:5:2])
print(l[:3])
print(l[2:])
print(l[1:4])
print(l[5::-1])
print(l[-1:-6:-1])
print(l[::-1])
print(l[0:5])
print(l[:])


# List
li1 = [10, 20, 30]
li2 = li1[:]

# Tuples
t1 = (10, 20, 30)
t2 = t1

# Si
s1 = "geeks"
s2 = s1[:]

print(li1 is li2)
print(t1 is t2)
print(s1 is s2)


