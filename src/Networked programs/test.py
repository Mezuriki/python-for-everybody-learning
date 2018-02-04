import socket, os

url = input("Enter the URL: ")
try:
    host = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    myrequest = 'GET '+ url + 'HTTP/1.0\r\n\r\n'
    mysock.send(myrequest.encode())
except:
    print("Enter the valid URL")


while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()



