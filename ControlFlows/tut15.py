# Different types of iterators provided by this module are:
# Infinite iterators
# Combinatoric iterators
# Terminating iterators

# 1.Infinite Iterators

# 1.count(start, step)
import itertools
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
print("\r")
# 2.cycle(iterable):
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count = count + 1
print("\r")
# Example 2: Using next function.
# Combinatoric iterators
l1 = ["Sarbodaya", "Dreamed", "To be an Officer"]
iterators = itertools.cycle(l1)

for i in range(6):
    print(next(iterators), end=" ")
