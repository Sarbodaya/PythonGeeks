# Implementation of Chaining In Python
class Myhash:
    def __init__(self, b):
        self.bucket = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.bucket
        self.table[i].append(x)

    def search(self, x):
        i = x % self.bucket
        return x in self.table[i]
    
    def remove(self,x):
        i = x % self.bucket
        if x in self.table[i]:
            self.table[i].remove(x)
        else:
            print(f"{x} is not present in tabele")
        

h = Myhash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)

print(h.search(56))
h.remove(56)
h.remove(56)
print(h.search(56))

