def missingPanagram(s):
    list1 = []
    a = s.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in alphabet:
            list1.append(i)
    return sorted(list1)


s = "Abcdefghijklmnopqrstuvwxy"
print(missingPanagram(s))
