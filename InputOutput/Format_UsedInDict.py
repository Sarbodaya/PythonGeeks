# Python Program to show format {} used in dictionary

tab = {"geeks": 2145, "for": 34, "geek": 99000}

print("Geeks : {0[geeks]:d}  for : {0[for]:d}  geek : {0[geek]:d}".format(tab))

data = dict(fun ="geeksforgeeks", adj ="portal")

# using format in dictionary
print("I love {fun} {adj}".format(**data))
