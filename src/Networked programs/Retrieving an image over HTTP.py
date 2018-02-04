import socket
import time

host = 'images-na.ssl-images-amazon.com'
port = 443
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))
mysock.sendall(b'GET https://images-na.ssl-images-amazon.com/images/M/MV5BMjIwMjg2NDYyNF5BMl5BanBnXkFtZTcwMzA2MDY2OA@@._V1_SY1000_CR0,0,1502,1000_AL_.jpg HTTPS/1.0\r\n\r\n')
count= 0
picture = b""

while True:
    data = mysock.recv(5120)
    if (len(data) < 1): break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

pos = picture.find(b'\r\n\r\n')
print('Header length', pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
fhand = open("stuff1.jpg", "wb")
fhand.write(picture)
fhand.close()