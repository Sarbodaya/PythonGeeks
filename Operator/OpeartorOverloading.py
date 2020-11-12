# Code 2
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a, self.b


ob1 = Complex(1, 5)
ob2 = Complex(2, 8)
ob3 = ob1 + ob2
print(ob3)


# Code 3 : Overloading Comparision Operator

class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False


ob4 = A(10)
ob5 = A(15)

if ob4 > ob5:
    print("ob1 is greater than ob2")
else:
    print("ob1 is less than ob2")

