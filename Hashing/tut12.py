# Subarray with 0 sum in Python
def isSUM(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(a[i:j]) == 0:
                return 1
    return False

def main():
    l1 = [4, 3, -2, 1, 1]
    res = isSUM(l1)
    if res == 1:
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()