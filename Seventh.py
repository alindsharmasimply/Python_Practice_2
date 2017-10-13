from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFFERSIZE = 1024
ADDRESS = (HOST, PORT)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDRESS)
server_socket.listen(5)

while True:
    print 'Waiting for connection...'
    client_socket, addr = server_socket.accept()
    print '....connected from:', addr

    while True:
        data = client_socket.recv(BUFFERSIZE)
        if not data:
            break
        client_socket.send('[%s] %s' % (ctime(), data))
    client_socket.close()
client_socket.close()
