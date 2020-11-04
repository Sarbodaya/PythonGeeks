l1 = [x for x in range(7)]
d1 = {x: x**3 for x in l1}
print(d1)

d2 = {x: f"ID{x}" for x in range(11)}
print(d2)

l2 = [101, 102, 103]
l3 = ["geeks", "for", "geeks"]
d3 = {l2[i]: l3[i] for i in range(len(l2))}
print(d3)

# zip() : mapping

d4 = dict(zip(l2, l3))
print(d4)

# Inverting a Dictionary (key becomes value) and values becomes key
d9 = {101: "Sarbodaya", 102: "Jena", 103: "GeeksForGeeks"}
d10 = {v: k for(k, v) in d9.items()}
print(d10)




