from socket import *


HOST = 'localhost'
PORT = 21567
BUFFERSIZE = 1024
ADDRESS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)

while True:
    data = raw_input('>> ')
    if not data:
        break
    client_socket.send(data)
    data = client_socket.recv(BUFFERSIZE)
    if not data:
        break
    print data

client_socket.close()
