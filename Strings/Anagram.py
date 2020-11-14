
def Anagram(s1,s2):
    for i in range(0,len(s2)):
        if s1[i] not in s2:
            print("NO")
            break
    else:
        print("YES")


s1 = input("Enter the text : ")
s2 = input("Enter the text : ")
Anagram(s1, s2)


# 2.Naive Method 
def Anagram1(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)

    return(s1 == s2)
# Time Complexity : O(n*logn)

# Efficient Soln : O(n)

def areAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0] * 256
    
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] += -1

    for x in count:
        if x != 0:
            return False
    return True


