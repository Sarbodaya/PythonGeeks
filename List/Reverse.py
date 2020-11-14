def Reverse(l1):
    l1.reverse()
    return l1

def ownMethod(l1):
    s = 0
    l = len(l1)-1
    while s < l:
        l1[s],l1[l] = l1[l],l1[s]
        s = s + 1
        l = l - 1



print("Enter the number : ")
l1 = [int(x) for x in input().split()]
ownMethod(l1)
#print("Reverse of list : ")
print(l1)

#print("Using reversed function : ")
new_l = list(reversed(l1))
print(new_l)

#print("Using slicing operation : ")
l2 = [10, 20, 30]
new_l = l2[::-1]
print(new_l)

