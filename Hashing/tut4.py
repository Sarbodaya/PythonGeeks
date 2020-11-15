# Open Addressing
# 1. No. of slots in Hash Table >= No. of keys to inserted
# 2. Cache Friendly
# 3 . 1.Linear Probing 2.Quadractic Probing 3.Double Hashing

# 1.Linear Probing
# Linearly Searching for Next Empty Slot 
# when there is collision

# Search Function : We compute hash Function we go that index and compare
# If we find, we return true , Otherwise we linearly search.
# We Stop when one of the three cases arises 1.Empty Slot 2.Key Found 3.Traverse through
# The whole table.

# Problem with simply making slot empty when we delete
# Just Make insert "Deleted"

# Clustering Problem (arises)
# How to Handle clustering Problem with Linear Probing
# 1.Quadratic Probing
# hash(key, i) = (h(key)+i^2) % m
# 2.Double Hashing
# hash(key, i) = (h1(key)+i*h2(key)) % m


# Double Hashing
# hash(key, i) = (h1(key) + ih2(key)) % m  i = 0,1,2,3,4............
# 1. No Clustering
# 2. Distribute the keys more uniformly than linear probing and Quadractic Hashing
# 3. If h2(key) is relatively prime to m, then it always finds a free slot if there is one.


# h1(key) = (key%7)
# h2(key) = 6 - (key % 6)


# void doubleHashing(key)
# {
#     if(table is full):
#         return error
#     probe = h1(key), offset = h2(key)
#     while(table[probe] is occupied)
#     probe = (probe+offset) % m

# table[probe] = m
# }
