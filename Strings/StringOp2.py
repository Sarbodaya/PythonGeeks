# Program 1 : Len,lower,upper
s1 = "geeks"
print(len(s1))

s2 = s1.upper()
print(s2)

s3 = s2.lower()
print(s3)

print(s1.islower())
print(s3.isupper())

# Program 2 : Startwith ,endwith
s = "GeeksForGeeks Python Course"
print(s.startswith("Geeks"))
print(s.endswith("Course"))

print(s.startswith("Geeks",1))
print(s.startswith("Geeks",8,len(s)))

# Program 3 : Split join
s1 = "geeks for geeks"
print(s1.split())
s2 = "geeks,for,geeks"
print(s2.split(","))

l1 = ["sarbodaya", "jena", "K18NS"]
print(" ".join(l1))
print(",".join(l1))
 
# Program 4 : Strip

s = "--------geeksforgeeks---------"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))

# Program 5 : Find
print(s.find("geeks"))
print(s.find("gfg"))
n = len(s1)
print(s.find("geeks",0,n))
