# Removal Programs on sets
s = {10, 20, 30, 40}
s.discard(30)
print(s)

s.remove(20)
print(s)

s.clear()
print(s)

s.add(50)
print(s)

del s

# Others Operation
s = {10, 20, 30, 40}
print(len(s))

print(20 in s)
print(40 not in s)

# Operations on two sets (Part : 1)
s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print(s1|s2) # Union : s1.union(s2)
print(s1 & s2) # Intersection : s1.intersection(s2)
print(s1 - s2) # Difference : s1.difference(s2)
print(s1 ^ s2) # Symmetric Difference 


# Operations on two sets (Part : 2)
s1 = {2, 4, 6, 8}
s2 = {4, 8}

print('disjoint sets:', s1.isdisjoint(s2)) # Returns True : If there is no common values among the sets

print('isSubset:', s1 <= s2)
print(s1.issubset(s2))

print('proper set:', s1 < s2)

print('s1 is superset of s2:', s1 >= s2)
print(s1.issuperset(s2))

print('s1 is proper superset of s2:', s1 > s2)

