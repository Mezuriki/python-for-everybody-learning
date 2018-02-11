"""
Exercise 1: Change the socket program socket1.py to prompt the user for the URL
so it can read any web page. You can use split('/') to break the URL into its
component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user enters
an improperly formatted or non-existent URL.
"""

import socket, os

url = input("Enter the URL: ")
try:
    host = url.split('/')
    if host[0]!= 'http:':
        host_url = host[0]
        url = 'http://'+host_url
    else:
        host_url = host[2]
    print(host_url, url)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_url, 80))
    mysock.send(('GET ' + url +' HTTP/1.0\r\n\r\n').encode())
    print(host)
except Exception:
    print("Entered URL is not valid")
    os.sys.exit(1)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()