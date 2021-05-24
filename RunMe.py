from subprocess import Popen
import os
import time

def cmd(name) -> None:
    Popen(["python3", name])

files = os.popen("ls").readlines()

pid = Popen(["python3","gatewayServer.py"]).pid

time.sleep(2)

for f in files:
    if "Device" in f:
        cmd(f.rstrip("\n"))









#Popen(["kill -9", str(pid)])
