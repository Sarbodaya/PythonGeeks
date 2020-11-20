import re

hand = open("regex_sum_1048620.txt")
x = list()
for line in hand:
    y = re.findall('[0-9]+', line)
    x = x + y

sum1 = 0
for z in x:
    sum1 = sum1 + int(z)
print(sum1)
