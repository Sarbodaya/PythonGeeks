def uniqueRows(input):

    # convert each list into tuple
    # we are mapping tuple function on each
    # of input row matrix
    input = map(tuple, input)

    # put all row in set
    result = set(input)

    # print all unique rows
    for row in list(result):
        print(row)



if __name__ == '__main__':
    input = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]
    uniqueRows(input)