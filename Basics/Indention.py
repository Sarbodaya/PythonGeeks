

site = 'gfg'
if site == 'gfg':
    print("Logging into geeksforgeeks .......")
else:
    print("Retype the url ...................")

print("All set .........")

j = 1
while(j<=5):
    print(j, end=" ")
    j = j + 1
print('\r')
a = 10; b = 20; c = b + a
print(a); print(b); print(c)

a = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

print(a)
# Example 2
# The following code is also valid

person_1 = 18
person_2 = 20
person_3 = 12

if (
        person_1 >= 18 and
        person_2 >= 18 and
        person_3 < 18
   ):
    print('2 Persons should have ID Cards')



# Explict Line Continuation
"""x = \
   1 + 2 \
    + 5 + 6 \
    + 10
print(x)"""
"""x = 10

flag = (x == 10)and(x <= 12)
print(flag)

# Example
x = [1, 2, 3]
y = 11
a = y in a
print(a)
"""
x = 10
while(x != 0):
    if(x > 5):
        print('x > 5')
    else:
        print('x < 5')
    x -= 2






