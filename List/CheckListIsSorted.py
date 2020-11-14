def isSorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            print("No")
            break
    else:
        print("Yes")

print("Enter the elements : ",end=" ")
l = [int(x) for x in input().split()]
print("Is Array Sorted : ")
isSorted(l)
