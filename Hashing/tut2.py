# Collision Handling
# 1. If we know the keys in advance, then we can do Perfect Hashing
# 2. If we do not know keys, then we use one of the following.
#    -->Chaining
#    -->Open Adressing : 1. Linear Probing 2.Quadratic Probing 3.Double Hashing


# Chaining
# Hash(key) = key % 7
# keys = {50, 21, 58, 17, 15, 49, 56, 22, 23, 25}

# Hash Table (Array of Linked List Headers)

# 0  |21-->49-->56
# 1  |50-->15-->22
# 2  |58-->23
# 3  |17 
# 4  |25
# 5  |
# 6  |

# Performance

# m : No. of slots in Hash Table
# n = No. of keys to be inserted

# Load factor : Alpha = n/m
# Expected Chain Length : Alpha
# Expected time search : O(1+Alpha)
# Expected Time To Insert/Delete : O(1+Alpha)



# Data Structures For Storing Chainings
# 1. Linked List
# 2. Dynamic Sized Arrays (Vector in c++, Array List In Java, List in Python)
# 3. Self Balancing BST : (AVL Tree, Red Black Tree) : O(log l)