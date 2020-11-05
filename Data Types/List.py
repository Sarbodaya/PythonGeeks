
# Creating a List
List = []
print("Blank List : ")
print(List)


List = [10, 20, 30]
print("\nList of numbers : ")
print(List)

# Knowing the size of list
print("Size of List : ")
print(len(List))

# Adding Elements into list

List.append(40)
List.append(50)
List.append(60)
print("List after Addition of three elements : ")
print(List)


# Adding elements to the list using iterator

for i in range(7, 11):
    List.append(i*10)

print("List After addition of 4 elements : ")
print(List)

# Adding tuple to the list

List.append((110, 120))
print("List after adding Tuples : ")
print(List)


# Adding List to the List

List2 = [130, 140]
List.append(List2)
print("List After Adding another List : ")
print(List)


# Using of Insert Method
# append() : Only works for the addition of elements in the end of the list
# insert() : This method adds the elements at the desired location it takes two arguments (position, value)

List.insert(0, "Geeks")
List.insert(1, "For")
List.insert(2, "Geeks")

print("List after performing Insert Operation : ")
print(List)


# Using of Extend Method
# extend() : Adding multiple elements at the end of the list at the same time
List.extend([8, 'Geeks', 'Always'])
print("List after performing Extend Operation : ")
print(List)




