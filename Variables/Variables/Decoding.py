# Decoding is process to convert a Byte object
# to String. It is implemented using decode().

a = "GeeksForGeeks"

c = b'GeeksForGeeks'  # Byte Object

d = c.decode('ASCII')
if d == a:
    print('Decoding Successful')
else:
    print("Decoding UnSuccessful")
