# Generators in Python
# Generator-Function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)


# Generator-Object :

def simpleGenerator():
    yield 1
    yield 2
    yield 3


x = simpleGenerator()
print(x.__next__())
print(x.__next__())
print(x.__next__())
