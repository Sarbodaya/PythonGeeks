
# When you want to take input of list of integers given in a single line
"""import  sys

def get_ints():
    return  list(map(int, sys.stdin.readline().strip().split()))

arr = get_ints()

sys.stdout.write(str(arr))"""

# When you want to take input of particular integers of integers given in a single line

import  sys

def get_ints():
    return map(int, sys.stdin.readline().strip().split())

x, y, z = get_ints()

sys.stdout.write(str(x))
print()
sys.stdout.write(str(y))
sys.stdout.write(str(z))








