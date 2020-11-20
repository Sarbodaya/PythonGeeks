# Switch Function
# To get around this fact, we use dictionary mapping.

def numbersTostring(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument)


if __name__ == '__main__':
    arguement = 0
    print(numbersTostring(arguement))
