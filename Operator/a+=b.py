# Python | a += b is not always a = a + b
# Example1
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]

print(list1)
print(list2)

# Example2
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

print(list1)
print(list2)

# 1.expression list1 += [1, 2, 3, 4] modifies the list in-place,
# means it extends the list such that “list1” and “list2” still have the reference to the same list.
# 2.expression list1 = list1 + [1, 2, 3, 4] creates a new list and
# changes “list1” reference to that new list and “list2” still refer to the old list.
