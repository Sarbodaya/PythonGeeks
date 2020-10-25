# Python code to demonstrate working of
# global and non local
a = 10
def read():
    print(a)
def mod1():
    global a
    a = 5
def mod2():
    a = 15

read()
mod1()
read()
mod2()
read()

# demonstrating non local
# inner loop changing the value of outer a
# prints 10

print("Value of a using nonlocal is : ", end=" ")
def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)

outer()

# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
print("Value of a without using local is : ", end=" ")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print(a)

outer()





