# Python Membership and Identity Operators | in, not in, is, is not
# 1.in operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("Overlapping")
else:
    print("Not Overlapping")


# Same Example using without using in operator
def overlapping(list3, list4):
    c = 0
    d = 0
    for i in list3:
        c += 1

    for i in list4:
        d += 1

    for i in range(0, c):
        for j in range(0, d):
            if list1[i] == list2[j]:
                return 1
    return 0


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
if overlapping(list1, list2):
    print("overlapping")
else:
    print("Not Overlapping")
