# Hash Table Data Structure
# Search  : O(1) on average
# Insert  : O(1) on average
# Delete  : O(1) on average

# Not Used for 
# 1. Finding Closet Value : AVL Tree or
# 2. Sorted Data          : Red Black Tree (self balancing tree)
# 3. Prefixing Searching  : Tri Data Structure

# Application of Hashing
# 1. Dictionary
# 2. Database Indexing
# 3. Cryptography
# 4. Caches
# 5. Symbol Tables in Compilers/Interpreter
# 6. Routers
# 7. Getting Data from Databases

# How Hash Function Works
# 1.Should always map a large key to small key.
# 2.Should Generate values from 0 to m-1.
# 3.Should be fast , O(1) for integers and O(len) for strings of length "len".
# 4.Should uniformly distribute large keys into Hash Table.

# Example of Hash Function
# 1. h(large_keys) = large_keys % m : m is chosen to be a prime number closet to the Hash Table
# 2. For strings, weighted sum : str[] = "abcd"
#   (str[0]*x^0 + str[1]*x^1 + str[2]*x^2 + str[3]*x^3) % m : m is a table size
# 3. Universal Hashing : Randomly picking a Hash Function From Set Of Hash Functions

