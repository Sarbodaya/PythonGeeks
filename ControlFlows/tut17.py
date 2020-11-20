listA = ['a', 'e', 'i', 'o', 'u']
iter_list = iter(listA)
try:
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
except Exception as e:
    print(e)

# Code 2
lst = [11, 23, 33, 44, 55]
iter_list = iter(lst)
while True:
    try:
        print(iter_list.__next__())
    except Exception as e:
        print(e)
        break
