# Python | Generator Expressions
# Python code to illustrate generator, yield() and next().
def generator():
    i = 1
    print(f"First Value is : {i}")
    yield i

    i += 1
    print(f"Second Value is : {i}")
    yield i

    i += 1
    print(f"Third Value is : {i}")
    yield i


obj = generator()
obj.__next__()
obj.__next__()
obj.__next__()
