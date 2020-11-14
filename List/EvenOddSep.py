def isEven(l):
    even = []
    odd = []
    for x in l:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd


l = [10, 12, 13, 15]

even, odd = isEven(l)
print("Even List : ")
print(even)
print("Odd List : ")
print(odd)
