import sys

from socket import * 

serverSocket = socket(AF_INET, SOCK_STREAM)

server_address=('localhost',8989)

serverSocket.bind(server_address)

serverSocket.listen(1)

print ('the cloud server is up on port:',8989)

while True:

    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket,addr)

    try:
        print(" [C] I got a message! \n")
        message = connectionSocket.recv(1024)
        if len(message) > 0: 
            print(message)
    except IOError:
        print("Doveva annà cosi fratelli")
 #Invia messaggio di risposta per file non trovato
