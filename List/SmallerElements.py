def getSmaller(List, x):
    small = []
    for i in List:
        if i < x:
            small.append(i)

    return small


List = [8, 100, 20, 40, 3, 7]
x = 30
print("Smaller Elements than", x, " : ")
print(getSmaller(List, x))
