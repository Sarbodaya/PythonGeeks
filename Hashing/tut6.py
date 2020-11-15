# Set In Python
# Set is a collection of item
# 1.Distinct Elements
# 2.Unordered : No Predefined order to print the elements
# 3.No Indexing
# 4.Union, Intersection , Set Difference
#   etc are fast.
# 5.Uses Hashing

s1 = {10, 20, 30}
print(s1)

s2 = set([40, 50, 60])
print(s2)

s3 = {}
print("Creates empty Dict: ")
print(type(s3))

s4 = set() # This creates an empty sets
print(type(s4))
print(s4)

s = {10, 20}
s.add(30)
print(s)

s.add(30)
print(s)

s.update([40, 50])
print(s)

s.update([60, 70], [80, 90])
print(s)


