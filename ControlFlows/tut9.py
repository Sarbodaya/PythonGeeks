# Using else conditional statement with for loop in python
# The else block just after for/while is executed
# only when the loop is NOT terminated by a break statement.

for i in range(1, 4):
    print(i)
else:
    print("No Break")
# Else block is not executed in Below Program
for i in range(1, 4):
    print(i)
    break
else:
    print("No Break")


# Program 2


def contains_even_number(a):
    for ele in a:
        if ele % 2 == 0:
            print("List contain even numbers")
            break
    else:
        print("List not contains even numbers")


if __name__ == '__main__':
    print("For List1 : ")
    contains_even_number([1, 9, 8])
    print("For List2 : ")
    contains_even_number([1, 3, 5])

# Exercise Predict the output
count = 0
while count < 1:
    count = count + 1
    print(count)
    break
else:
    print("No Break")
