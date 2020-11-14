# 1.Method Through Slicing
def leftRotate(l1,r):
    l1 = l1[r:]+ l1[:r]
    print(l1)

# 2.OwnMethod
def leftRotate1(l1,r):
    for i in range(0,r):
        l1.append(l1.pop(0))



l1 = [int(x) for x in input().split()]
r = int(input())
leftRotate1(l1, r)
print(l1)
