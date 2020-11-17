# ii) zip function (Both iterators to be used in single looping construct):
cars = ['Aston', 'Audi', 'McLaren']
accessories = ['GPS', 'Car Repair Kit', 'Dolby Sound Kit']
for i, j in zip(cars, accessories):
    print(f"Car: {i}  Accessory Required: {j}")

# Python program to demonstrate unzip (reverse
# of zip)using * with zip function 

# Unzip lists
l1, l2 = zip(*[('Aston', 'GPS'),
               ('Audi', 'Car Repair'),
               ('McLaren', 'Dolby sound kit')])

# Printing unzipped lists
print(l1)
print(l2)
