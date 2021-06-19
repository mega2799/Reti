import IOTdevice
import schedule
import time

def run():
    obj = IOTdevice.Device("Odin", '192.168.1.5')
    return obj

def connectAndUpdate(dev) -> None:
    dev.connect(device.toString())
    dev.updateData()


if __name__ == "__main__":
    device = run()
    schedule.every(5).seconds.do(connectAndUpdate, device)

    while True:
        schedule.run_pending()
        time.sleep(1)
