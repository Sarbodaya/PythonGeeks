# We use two operators *(for tuples) **(for Dict)
# Unpacking
# We can use * to unpack the list so that all
# elements of it can be passed as different parameters.


def fun(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]
# fun(my_list) : This will throw error
fun(*my_list)

args = range(3, 6)
print(*args)


# Packing
# A Python program to demonstrate use
# of packing
# This function uses packing to sum
# unknown number of arguments
def sum(*numbers):
    sum1 = 0
    for i in range(0, len(numbers)):
        sum1 += numbers[i]

    return sum1


print(sum(1, 2, 3, 4, 5, 6))
print(sum(10, 20))
