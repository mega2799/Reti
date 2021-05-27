import sys

from socket import * 

DEBUG = False

serverSocket = socket(AF_INET, SOCK_STREAM)

server_address=('localhost',8989)

serverSocket.bind(server_address)

serverSocket.listen(1)

print ('the cloud server is up on port:',8989)

while True:

    connectionSocket, addr = serverSocket.accept()
    if DEBUG:
        print(connectionSocket,addr)

    try:
        if DEBUG:
            print(" [C] I got a message! \n")
        message = connectionSocket.recv(1024)
        if len(message) > 0 and DEBUG : 
            print(message.split())
        
        dataList = message.split()
        
        if len(dataList) > 0:
            print(dataList[0].decode('utf-8'))

    except IOError:
        print("Doveva annà cosi fratelli")
