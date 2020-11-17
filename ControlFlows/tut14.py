# Python Itertools

import operator
import time

L1 = [2, 4, 8]
L2 = [6, 7, 10]
# Starting time before map
# function
t1 = time.time()
a, b, c = map(operator.mul, L1, L2)
t2 = time.time()
print(f"Result : {a} {b} {c}")
print("Time taken by map function : %.6f" % (t2 - t1))

# Starting Time for naive method
t1 = time.time()
print("Result : ", end=" ")
for i in range(len(L1)):
    print(L1[i] * L2[i], end=" ")

t2 = time.time()
print("\nTime taken by map function : %.6f" % (t2 - t1))
