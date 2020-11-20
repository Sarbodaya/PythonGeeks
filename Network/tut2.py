import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = 'http://h2020.myspecies.info/'
mySock.connect((url, 80))
cmd = 'GET http://h2020.myspecies.info/ HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mySock.close()
