# repeat(val, num): This iterator repeatedly prints the passed value infinite
# number of times. If the optional keyword num is mentioned, then it repeatedly
# prints num number of times.
import itertools
from itertools import product
print("Printing the number repeatedly : ")
print(list(itertools.repeat(25, 4)))

# Combinatoric iterators
# In Python there are 4 combinatoric iterators:

# 1.Product
print("The cartesian Product using repeat : ")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the container : ")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the container : ")
print(list(product('AB', [3, 4])))
