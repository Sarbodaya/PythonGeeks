listb = ['Cat', 'Dog', 'Sat', 'Mat']
iter_listb = listb.__iter__()
try:
    print(iter_listb.__next__())
    print(iter_listb.__next__())
    print(iter_listb.__next__())
    print(iter_listb.__next__())
    print(iter_listb.__next__())
except Exception as e:
    print(e)
    print("\nThrowing 'StopIterationError")
