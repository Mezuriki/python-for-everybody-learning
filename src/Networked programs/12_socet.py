import socket, os

url = input("Enter the URL: ")
try:
    host = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(host, 80)
    mysock.send('GET' + url +'HTTP/1.0\r\n\r\n'.encode())
    print(host)
except:
    print("Entered URL is not valid")
    os.sys.exit(1)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()