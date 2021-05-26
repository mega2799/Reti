import IOTdevice
import schedule
import time

def run():
    obj = IOTdevice.Device("Promethues", 'localhost')
    return obj

def connectAndUpdate(dev) -> None:
    dev.connect(device.toString())
    dev.updateData()


if __name__ == "__main__":
    device = run()
    schedule.every(2).seconds.do(connectAndUpdate, device)

    while True:
        schedule.run_pending()
        time.sleep(1)
