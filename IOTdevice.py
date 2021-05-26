import socket as s
from datetime import datetime, timedelta
import random
import schedule
import time

gatewayAddress = 'localhost'

class Device:
    name: str 
    ip : str
    data : list 
    day : datetime
    temperature: int
    humidity: int

    def toString(self) -> str:
        message = self.name + " "
        message += self.ip + " "
        message += self.data[0] + " "
        message += str(self.data[1]) + " "
        message += str(self.data[2]) + " "
        return message
       
    def connect(self, message) -> None:
        sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
        gateway = (gatewayAddress, 9898)
        send = sock.sendto(message.encode(), gateway)
 
    def __init__(self, divinity: str, ip: str) -> None:
        self.name = divinity
        self.ip = ip
        print("[D]\tHi my name is: " + self.name + "\tip: " + self.ip)
        self.day = datetime.now()
        self.data = [self.day.strftime("%Y-%m-%d at %H:%M"), 19, 17 ]
       
    def updateData(self) -> None:
        self.day = self.day + timedelta(1, 0)
        self.data = [self.day.strftime("%Y-%m-%d at %H:%M"), random.randint(-2, 35), random.randint(1,99)]

"""
    def scheduleMe(self) -> None:
        schedule.every(10).seconds.do(self.connect(self.toString()))       
        while True:
            schedule.run_pending()
            time.sleep(1)
"""   
