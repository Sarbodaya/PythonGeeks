fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)

# Creating an iterator object
# from that iterable i.e fruits
fruits = ["mango", "banana", "grapes"]
iter_obj = iter(fruits)

while True:
    try:

        # getting the next item
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        # if StopIteration is raised,
        # break from loop
        break
