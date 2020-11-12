# Any
# Returns true if any of the items is True.
# It returns False if empty or all are false.
# Any can be thought of as a sequence of OR operations on the provided iterables.
# It short circuit the execution i.e. stop the execution as soon as the result is known
print("ANY Function : ")
# Since all are False so False is returned
print(any([False, False, False, False, False, False]))
print(any([]))
# Here the Second Method will short - circuit at the
# second item( True) and will return True
print(any([False, True, False, False, False]))
print(any([True, False, False, False, False]))

# ALL
print("ALL Function : ")
# Returns true if all of the items are True (or if the iterable is empty).
# All can be thought of as a sequence of AND operations on
# the provided iterables. It also short circuit the execution
# i.e. stop the execution as soon as the result is known.
print(all([True, True, True, True]))
print(all([False, False, True]))
print(all([False, False, False]))

print("Practical Example")
# This code explains how can we
# use 'any' function on list

list1 = []
list2 = []

for i in range(1, 11):
    list1.append(4*i)

for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print(any(list2))
print(all(list2))
