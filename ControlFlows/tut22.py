def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


for element in [34, [1, 3], (45, 78), {1: "ABC"}, "sarbodaya", 8.9]:
    print(f"{element} is iterable : ", iterable(element))
