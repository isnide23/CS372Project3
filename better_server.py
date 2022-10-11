from socket import *

message = "HTTP/1.1 200 OK\r\n"\
"Content-Type: text/plain\r\n"\
"Content-Length: 6\r\n"\
"Connection: close\r\n"\
"\r\n"\
"Hello!"

serverPort = 12000
serverSocket = socket()
serverSocket.bind(('', serverPort))
serverSocket.listen()

while True:
    connectSocket, info = serverSocket.accept()
    print(connectSocket)
    buffer = b""
    while True:
        data = connectSocket.recv(10)
        buffer+= data
        if  b"\r\n\r\n" in buffer:
            break
    print(buffer.decode("ISO-8859-1"))
    connectSocket.sendall(message.encode("ISO-8859-1"))
    connectSocket.close()