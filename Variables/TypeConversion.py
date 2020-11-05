# 1. int(a,base) : This function converts any data type to
# integer. ‘Base’ specifies the base in which string is if data type is string.
#
# 2. float() : This function is used to convert any data
# type to a floating point number

s = "10010"
c = int(s, 2)
print("After converting to integer base 2 : ", c)

e = float(s)
print("After converting to float : ", e)

# 3. ord() : This function is used to convert a character to integer.
# 4. hex() : This function is to convert integer to hexadecimal string.
# 5. oct() : This function is to convert integer to octal string.

s = '4'
c = ord(s)
print('After converting a character to integer : ', c)

c = hex(56)
print('After converting a integer to hexadecimal string : ', c)

c = oct(56)
print('After converting a integer to octal string : ', c)


