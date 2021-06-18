import sys

from socket import * 

import tkinter as tk

from IOTdevice import Device

from datetime import datetime

DEBUG = False

serverSocket = socket(AF_INET, SOCK_STREAM)

server_address=('localhost',8989)

serverSocket.bind(server_address)

serverSocket.listen(1)

print ('[C] the cloud server is listening up on port:',8989)

tmp = Device("tempDevice", "local")

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
        
        dataList = [elem.decode('utf-8') for elem in message.split()]
        
        #[print(Device.autentication(dataList[k], dataList[k+3], dataList[k +4], dataList[k+5])) for k in dataList]

        #print("Name ----------------- Time --------------- Humidity --------------- Temperature")
        for k in range(0,len(dataList),6):
            print("-----------------------------------------------------------------------------------")   
            print("Name  |        Date      |       Time  |         Humidity  |   Temperature")
            actual = datetime.strptime(datetime.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
            
            print(tmp.autentication(dataList[k], dataList[k+2], dataList[k+3], dataList[k +4], dataList[k+5]))

            delay = (actual - datetime.strptime(dataList[k+3], "%H:%M:%S.%f")).total_seconds()

            print(f'\n il device {dataList[k]} ha {delay= }')

    except IOError:
        print("Error Occurred")
        sys.exit
