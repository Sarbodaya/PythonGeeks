def onlyOdd(l):
    l1 = [int(x) for x in l if x % 2 != 0]
    return l1

print("Enter the numbers : ")
l = [int(x) for x in input().split()]
result = onlyOdd(l)
print(result)

