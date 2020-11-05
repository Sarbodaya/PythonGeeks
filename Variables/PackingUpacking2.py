# A Python
# program to
# demonstrate both packing and
# unpacking.
# A sample python function that takes three arguments
# and prints them


def unpacking(a, b, c):
    print(a, b, c)


def packing(*args):
    args = list(args)
    args[0] = 'GeeksForGeeks'
    args[1] = 'awesome'

    unpacking(*args)


packing('Hello', 'Sarbodaya', 'Jena')


# ** is used for dictionaries
# A sample program to demonstrate unpacking of
# dictionary items using **
def fun2(a, b, c):
    print("Unpacking of Dict : ")
    print(a, b, c)


# dict1 = {'Hello': 1, 'Geeks': 2, 'Guys': 3}
d = {'a': 2, 'b': 4, 'c': 10}
fun2(**d)


# A Python program to demonstrate packing of
# dictionary items using **

def fun4(**kwargs):
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))


fun4(name="Sarbodaya", ID="11804093", language="Python")











