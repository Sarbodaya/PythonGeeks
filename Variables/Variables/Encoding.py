# 1.Byte Objects are  sequence of Bytes
# Strings are sequence of characters.

# 2.Byte objects are in machine readable form
# internally, Strings are only in human readable form.

# 3.Since Byte objects are machine readable, they can be
# directly stored on the disk. Whereas, Strings need encoding
# before which they can be stored on disk.

# PNG, JPEG, MP3, WAV, ASCII, UTF-8 etc are different forms of encodings.
# An encoding is a format to represent audio, images, text, etc in bytes.
a = 'GeeksForGeeks'
# Initializing a byte Object
c = b'GeeksForGeeks'

# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d = a.encode('ASCII')

# Checking if a is converted to bytes or not
if c == d:
    print("Encoding Successful")
else:
    print('UnSuccessful')






