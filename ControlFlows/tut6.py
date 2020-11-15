# range() vs xrange() in Python
# range() and xrange() are two functions that could be used to iterate a certain number of times
# in for loops in Python. In Python 3,
# there is no xrange , but the range function behaves like xrange in Python 2.
import sys
a = range(1, 10000)

print("The return type of range() is : ")
print(type(a))

# Memory
print("The size allotted using range() is : ")
print(sys.getsizeof(a))

# Operations usage
# As range() returns the list, all the operations that can be applied on the list can be used
# on it. On the other hand, as xrange() returns the xrange object, operations associated to
# list cannot be applied on them, hence a disadvantage.

a = range(1, 6)
print("The list after slicing using range is : ")
print(a[2:5])
