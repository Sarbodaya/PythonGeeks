for i in ['Berlin', 'Vienna', 'Zurich']:
    print(i)
print("\n")
for i in ("Python", "Perl", "Ruby"):
    print(i)

for char in "Iteration is Easy":
    print(char, end="")

print("\n")
cities = ["SARBODAYA", "JENA", "Junior"]
a = iter(cities)
print(next(a))
print(next(a))
print(next(a))
