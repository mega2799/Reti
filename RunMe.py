from subprocess import Popen
import os
import time

def cmd(name) -> None:
    Popen(["python3", name])

files = os.popen("ls").readlines()

pid = Popen(["python3","gatewayServer.py"]).pid

time.sleep(2)

# Accende i vari device
for f in files:
    if "Device" in f:
        cmd(f.rstrip("\n"))


# Uccide il processo sel server che altrimenti rimarrebbe in ascolto
input("Exit [Y/Y]")
os.popen("kill -9 " + str(pid)) 
