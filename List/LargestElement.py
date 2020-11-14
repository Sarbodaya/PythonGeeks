# To find the largest element in List
# there is direct function : max()

l = [10, 5, 6, 8, 9]
print(max(l))



# 1st Method
def getMax(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None

a = getMax(l)
print("Method 1 : ")
print("Maximum Element : ", a)




# 2nd Method
def getMax1(l):
    if not l:
        return None

    else:
        res = l[0]
        for i in range(1,len(l)):
            if res < l[i]:
                res = l[i]
        return res

b = getMax1(l)
print("Method 2 : ")
print("Maximum Element : ", b)

