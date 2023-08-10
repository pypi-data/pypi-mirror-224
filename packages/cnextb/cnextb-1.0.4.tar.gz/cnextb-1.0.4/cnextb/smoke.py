from cnextb.device import *
import time

if __name__ == '__main__':
    dev = scanDevices()
    dev_str = ''
    for ele in dev.keys():
        if 'USB' in ele:
            dev_str = ele
            break
    cnexdev = CnextbDevice(dev_str)
    cnexdev.executeAndCheckCommand("power down")
    time.sleep(3)
    cnexdev.executeAndCheckCommand("power up")

