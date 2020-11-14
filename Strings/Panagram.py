def isPanagram(s):
    arr= {}

    for i in range(0,len(s)):
        arr[s[i].lower()] = 1

    if len(arr) == 26:
        return 1
    else:
        return 0



if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(isPanagram(s))
        t = t - 1


    