text = input("Enter the text : ")
s = 0
l = len(text)-1

while s < l:
    if text[s] != text[l]:
        print("NO")
        break
    s = s + 1
    l = l - 1
else:
    print("Yes")


#. Shortcut Program
if text == text[::-1]:
    print("YES")
else:
    print("NO")

