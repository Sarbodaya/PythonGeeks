
# 1.Naive Method
def getMax(l):
    return max(l)

def secondMax(l):
    if len(l) < 1:
        return None
    largest = getMax(l)
    result = -1
    for i in l:
        if i != largest:
            if result == -1:
                result = i
            elif i > result:
                result = i
    return result            

# 2.Second Method : One Traversal Method
def secondMax1(l):
    if not l:
        return None
    lar = l[0]
    slar = None
    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or (slar < x):
                slar = x
    return slar



print("Enter the numbers : ")
l = [int(x) for x in input().split()]
c = secondMax1(l)
print("Second Largest element : ", c)

