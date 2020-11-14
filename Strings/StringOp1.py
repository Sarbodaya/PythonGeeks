# 1.Check For Substring
s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)
print(s2 not in s1)

# 2.Conatenation
s1 = "geeks"
s2 = "forgeeks"

s3 = s1 + s2
s4 = "Welcome to " + s1 + s2

print(s3)
print(s4)

# 3.Find the postion of the string
s1 = "geeksforgeeks"
s2 = "geeks"

print(s1.index(s2))
print(s1.rindex(s2)) # Last index where s2 is present
print(s1.index(s2,0,13)) # Search Starts from index 0
print(s1.index(s2,1,13)) # Seatch Starts from index 1




