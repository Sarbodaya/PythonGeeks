# Count Distinct Elements using Lists and Slicing
def Dis(a):
    count = 1
    for i in range(1,len(a)):
        if a[i] not in a[0:i]:
            count = count + 1
    return count

def main():
    a = [int(x) for x in input().split()]
    res = Dis(a)
    print(res)
if __name__ == "__main__":
    main()  