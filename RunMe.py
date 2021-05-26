from subprocess import Popen
import os
import time

pids = []

def cmd(name) -> None:
    pids.append(Popen(["python3", name]).pid)

files = os.popen("ls").readlines()

pids.append(Popen(["python3","gatewayServer.py"]).pid)

time.sleep(2)

# Accende i vari device
for f in files:
    if "Device" in f:
        cmd(f.rstrip("\n"))


# Uccide i processi che altrimenti rimarrebbero attivi
input("Exit [Y/Y]")

#os.popen("kill -9 " + str(pids)) 

[os.popen("kill -9 " + str(i)) for i in pids]
