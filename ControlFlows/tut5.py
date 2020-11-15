king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya', 'Modi': 'The Changer'}
for key, value in king.items():
    print(key, value)

# Using sorted():  sorted() is used to print the container is sorted order. It doesn’t
# sort the container but just prints the container in sorted order for 1 instance.
# The use of set() can be combined to remove duplicate occurrences.

lis = [1, 3, 5, 6, 2, 1, 3]
print("The List in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")

print("\r")

print("The List in sorted order (Without Duplicates) is ")
for i in sorted(set(lis)):
    print(i, end=" ")
print("\r")

# Example 1
basket = ['guava', 'orange', 'apple', 'pear', 'guava', 'banana', 'grape']
for i in sorted(set(basket)):
    print(i, end=" ")

print("\r")
# Example 2
lis = [1, 3, 5, 7, 9, 11, 13]
print("The List in reversed order : ")
for i in reversed(lis):
    print(i, end=" ")

# Example 3
print("Reversed Range : ")
for i in reversed(range(1, 10, 3)):
    print(i, end=" ")




