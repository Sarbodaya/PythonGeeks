text = input("Enter the text : ")
patt = input("Enter the patt : ")

pos = text.find(patt)
while pos >= 0:
    print(pos)
    pos = text.find(patt,pos+1)
    
