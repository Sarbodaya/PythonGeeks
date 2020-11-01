def Replace(string1):
    string1 = string1.replace(',', "third")
    string1 = string1.replace('.', ',')
    string1 = string1.replace('third', '.')
    return string1


string1 = "14, 625, 498.002"
print(Replace(string1))

# Replace Function


