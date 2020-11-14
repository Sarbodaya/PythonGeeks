# cook your dish here
def Ans(q,n,k):
    lefQ = 0
    for i in range(0,len(q)):
        if q[i] > k:
            lefQ = q[i] + lefQ
            lefQ = q[i] - k
        elif q[i] == k:
            lefQ = lefQ + q[i]
            lefQ = lefQ - k
        else:
            lefQ = lefQ + q[i]
            if lefQ >= q[i]:
                lefQ = lefQ - k
            else:
                return i+1
            
def printList(q):
    for i in q:
        print(i, end=" ")          
            
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        k = int(input())
        q = []
        for i in range(0,n):
            x = int(input())
            q.append(x)
        printList(q)
        t = t - 1
        

if __name__ == '__main__':
    main()