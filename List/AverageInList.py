def Avg(list):
    c = len(list)
    z = sum(list)
    return z/c


def Average(list):
    sum = 0
    for x in list:
        sum = sum + x
    n = len(list)
    return sum/n



list = [10, 20, 30, 40]
print("Average : ")
print(Average(list))

