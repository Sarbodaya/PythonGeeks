"""# Normal Method

n = int(input())

arr = [int(x) for x in input().split()]

summation = 0
for x in arr:
    summation = summation + x
print("Sum of integer arrays : ", summation)"""

# A bit faster method using inbuilt stdin, stdout:

# import inbuilt standard input output
from sys import stdin, stdout

def Main():
    # input via readline method
    n = stdin.readline()

    # array input similar method
    arr = [int(x) for x in stdin.readline().split()]
    summation = 0

    # calculate sum
    for x in arr:
        summation += x

    stdout.write(str(summation))

if __name__ == '__main__':
    Main()

