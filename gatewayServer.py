import socket as sk

import time

DEBUG = False 

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 9898)

print ('[G] gateway starting up on %s port %s' % server_address)

sock.bind(server_address)

while True:
    if DEBUG:
        print('[G] gateway waiting to receive message from the devices')

    data, address = sock.recvfrom(4096)

    listData = data.decode('utf-8').split(" ")

    if DEBUG:
        print('\n**[G]** received %s bytes from %s' % (len(data), address))

        print(listData)

