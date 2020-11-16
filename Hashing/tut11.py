# Subarray with 0 sum in Python
def sub(l1):
    
    for i in range(1,len(l1)):
        sum = l1[i-1]
        for j in range(i,len(l1)):
            sum = sum + l1[j]
            if sum == 0:
                return 1
    return 0

def main():
    l1 = [4, 3, -2, 1, 1]
    res = sub(l1)
    if res == 1:
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()