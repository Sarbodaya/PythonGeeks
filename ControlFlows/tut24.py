def fib(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a + b


x = fib(10)
for i in range(10):
    try:
        print(x.__next__())
    except Exception as e:
        print(e)
