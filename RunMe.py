#!/usr/bin/python3 

from subprocess import Popen

import os

import time

pids = []

def cmd(name) -> None:
    pids.append(Popen(["python3", name]).pid)

files = os.popen("ls").readlines()

pids.append(Popen(["python3","cloudServer.py"]).pid)

pids.append(Popen(["python3","gatewayServer.py"]).pid)

#time.sleep(2)

# Accende i vari device
for f in files:
    if "Device" in f:
        cmd(f.rstrip("\n"))


# Uccide i processi che altrimenti rimarrebbero attivi
input("Press Enter or a character to stop everthing\n")

# Potrebbe uccidere anche processi non relativi all'elaborato ma molto comodo comunque
#os.popen("killall python3")

[os.popen("kill -9 " + str(i)) for i in pids]
