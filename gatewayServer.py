import socket as sk

import time

DEBUG = False 

BufferDim = 4096

#UDP server
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 9898)

# Cloud server
client_address = ('localhost', 8989)

print("[G] gateway starting up on %s port %s" % server_address)

print("[G] Buffer Dimension: ", BufferDim) 

sock.bind(server_address)

devicesCounter = 0

lecture = []

while True:
    if DEBUG:
        print('[G] gateway waiting to receive message from the devices')

    data, address = sock.recvfrom(BufferDim)

 #   listData = data.decode('utf-8').split(" ")

    if DEBUG:
        print('\n**[G]** received %s bytes from %s' % (len(data), address))

  #  listData = [str.encode(elem) for elem in listData]
    
    devicesCounter += 1
    lecture.append(data)
    if DEBUG:
        print("got data: ", devicesCounter)
    # I dati vengono inviati solo quando vengono ricevuti da tutti i device
    if devicesCounter == 4:
        # TCP client
        clientsocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

        try:
            clientsocket.connect(client_address)
        except Exception as err:
            print("bad Luck")
        
        time1 = time.perf_counter()
        [clientsocket.send(f) for f in lecture]
        time2 = time.perf_counter()
        print("[G] tempo impiegato per la trasmissione: ", time2 - time1)
        clientsocket.close()

        devicesCounter = 0
        lecture.clear()
