# Count Distinct Elements using Sets
def cDistinct(a):
    a = len(set(a))
    return a

a = [10, 20, 10, 30, 30, 20]
print("Distinct Elements : ",end=" ")
res = cDistinct(a)
print(res)
