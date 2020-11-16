# Dictinory in Python
# 1.Unordered 
# 2.Collection of key-Value pair
# 3.All keys must be distinct
# 4.Values may be repeated
# 5.Uses Hashing Internally
# 6.Dict is mutable

# Program 1 
d = {110:"abc", 115:"bca", 146:"dba", 150:"abc"}
print(d)
d = {}
d["apple"] = 1000
d["orange"] = 2000
d["grapes"] = 450
d["pears"] = 1001
print(d)
print(d["apple"])

# Program 2
print(d.get("apple"))
print(d.get(111))
print(d.get(111,"NA"))

if "orange" in d:
    print(d["orange"])
else:
    print("NA")

print()
print()
# Program 3
d = {}
d = {110:"abc", 101:"xyz", 105:"pqr", 106:"bcd"}
d[101] = "Indian Army"
print(d)
print(len(d))
print(d.pop(106))
print(d)
del d[110]
print(d)
d[108] = "Indian Navy"
print(d.popitem())
