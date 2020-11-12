# Consider that we have two objects which are a physical representation of a class
# (user-defined data type) and we have to add two objects with binary ‘+’ operator
# it throws an error, because compiler don’t know
# how to add two objects. So we define a method for an operator and that process is
# called operator overloading.

# Python Program illustrate how
# to overload an binary + operator
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
obj4 = A("ForGeeks")

print(ob1 + ob2)
print(ob3 + obj4)
