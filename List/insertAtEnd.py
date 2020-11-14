def insertAtEnd(arr, sizeOfArray, element):
    arr.append(element)
    return arr


def main():
    testCase = int(input())
    while testCase > 0:
        sizeOfArray = int(input())

        arr = [int(x) for x in input().strip().split()]
        element = int(input())
        insertAtEnd(arr, sizeOfArray, element)
        for i in arr:
            print(i, end=" ")

        testCase -= 1


if __name__ == '__main__':
    main()
