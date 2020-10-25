# Python program processing global variable
count = 5
def some_method():
    global count
    count = count + 1
    print(count)

some_method()

# Python program showing a scope of object
def some_function():
    print("Inside some function")
    def some_inner_func():
        var = 10
        print("Inside inner function the value of var : ", var)
    some_inner_func()
    print("Try printing var from outside function : ",var)

some_function()




