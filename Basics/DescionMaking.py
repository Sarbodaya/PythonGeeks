i = 10
if (i > 15):
    print("I am im IF Block")
print("I am not in IF BLOCK")

# Nested if
i = 10
if (i == 10):
    #  First if statement
    if (i < 15):
        print(i, " is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print(i, " is smaller than 12 too")
    else:
        print(i, " is greater than 15")

i = 10
if i < 15: print(i, "is less than 15")

# Short Hand if-else statement

i = 100
print(True) if i > 50 else print(False)

