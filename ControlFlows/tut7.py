# Programs for printing pyramid patterns in Python
# Simple Pyramid Pattern
def pyramid(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")


n = 6
pyramid(n)


# Another Approach :

def pypart(n):
    myList = []
    for i in range(1, n + 1):
        myList.append("* " * i)
    print("\n".join(myList))


n = 10
pypart(4)
