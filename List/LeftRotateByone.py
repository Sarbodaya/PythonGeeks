# Left Rotate By One
# Using Direct Method
# Through Slicing
l = [10, 20, 30, 40, 50]
l = l[1: ] + l[:1]
print(l)
# Through Append and POP
l = [10, 20, 30, 40]
l.append(l.pop(0))
print(l)


# Own method
def RotateByOne(l1):
    a = l1[0]
    for i in range(1, len(l1)):
        l1[i-1] = l1[i]
    l1.pop(len(l1)-1)
    l1.append(a)



l1 = [int(x) for x in input().split()]
RotateByOne(l1)
print(l1)
