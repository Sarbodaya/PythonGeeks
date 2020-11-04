l1 = [x for x in range(11) if x % 2 == 0]
print("Comprehensive Code for Even number : ")
print(l1)

l2 = [x for x in range(12) if x % 2 != 0]
print("Odd Numbers")
print(l2)


# Question using Comprehensive
def getSmaller(List, element):
    l1 = [x for x in List if x > element]
    l2 = [x for x in List if x < element]
    return l2, l1


List = [10, 20, 30, 40, 50, 60, 70, 80]
element = 40
l1, l2 = getSmaller(List, element)
print("Smaller elements than ", element, ": ")
print(l1)
print("Greater elements than ", element, ": ")
print(l2)
