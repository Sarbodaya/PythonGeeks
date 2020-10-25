# Python code to demonstrate working of
# in and is
# using "in" to check
if 's' in "geeksforgeeks":
    print("s is a part of geeksforgeeks")
else:
    print("s is not a part of geeks")
# using "in" to loop through
for i in "geeksforgeeks":
    print(i, end=" ")
print("\r")


# using is to check object identity
# string is immutable(once allocated cannot be changed)
# hence occupy same memory location
print(' ' is ' ')

# u sing is to check object identity
# dict is mutable(can be changed once allocated)
# hence occupy different memory location

print({} is {})


