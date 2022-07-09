import socket

host = socket.gethostname()
port = 12345
BUFFER_SIZE = 1024
MENSAGE = "Holaaaaasssss mundo"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host,port))
    socket_tcp.send(MENSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)
    print(data)