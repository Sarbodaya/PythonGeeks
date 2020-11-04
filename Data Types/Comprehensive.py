l1 = [x for x in range(11) if x%2 == 0]
print("Even number list : ")
print(l1)


l2 = [x for x in range(11) if x%2 != 0]
print("Odd number list : ")
print(l2)

s = 'geeksforgeeks'
l3 = [x for x in s if x in "aeiou"]
print("List containing vowels : ")
print(l3)

l4 = ["geeks", "ide", "courses", "gfg"]
l5 = [x for x in l4 if x.startswith('g')]
print("List containing letters starts with : ")
print(l5)

l6 = [x*2 for x in range(5)]
print('Table of 2 : ')
print(l6)

# Converting a list in Uppercase
l8 = ['geeks', 'for', 'geeks', 'genjutsu']
l7 = [x.upper() for x in l8 if x.startswith('g')]
print(l7)

# Creating a two sets
# List Comprehension
l13 = [x for x in range(20)]
l10 = {x for x in l13 if x % 2 == 0}
l11 = {x for x in l13 if x % 2 != 0}
print('Set 1 for even numbers : ')
print(l10)
print('Set 2 for odd numbers : ')
print(l11)


