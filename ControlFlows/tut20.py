# User_defined Objects
class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


if __name__ == '__main__':
    a, b = 3, 7

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    print("Print the range without iter()")
    for i in c1:
        print("Eating more Pizzas, counting : ", i, end="\n")

    print("Print the range with using iterator : ")
    obj = iter(c2)
    try:
        while True:
            print("Eating more Pizzas, counting : ", next(obj))
    except Exception as e:
        print(e)
        print("\nDead and overFood, Game Over")
