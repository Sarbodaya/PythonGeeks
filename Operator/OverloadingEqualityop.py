class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):  # Python Magic function for operator Overloading
        if self.a < other.a:
            return "ob1 is less than ob2"
        else:
            return "ob1 is greater than ob2"

    def __eq__(self, other):  # Python Magic function for operator Overloading
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Both are not equal"


ob1 = A(100)
ob2 = A(120)
print(ob1 < ob2)

ob3 = A(140)
ob4 = A(100)
print(ob3 == ob4)



