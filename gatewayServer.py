import socket as sk

import time

DEBUG = False 

#UDP server
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 9898)

client_address = ('localhost', 8989)

print ('[G] gateway starting up on %s port %s' % server_address)

sock.bind(server_address)

while True:
    if DEBUG:
        print('[G] gateway waiting to receive message from the devices')

    data, address = sock.recvfrom(4096)

    #listData = data.decode('utf-8').split(" ")

    if DEBUG:
        print('\n**[G]** received %s bytes from %s' % (len(data), address))

#    if len(listData) == 0:
#        SystemExit

    #listData = [str.encode(elem) for elem in listData]

    #TCP client
    clientsocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    try:
        clientsocket.connect(client_address)
    except Exception as err:
        print("bad Luckke")

    clientsocket.send(data)

    clientsocket.close()
