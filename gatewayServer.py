import socket as sk

import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 9898)

print ('[G] gateway starting up on %s port %s' % server_address)

sock.bind(server_address)

while True:
    print('[G] gateway waiting to receive message from the devices')

    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))

    print (data.decode('utf8'))
