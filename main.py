import adbutils

import android_boy

if __name__ == '__main__':
    adb = adbutils.AdbClient('127.0.0.1', 5037)
    boy_list = []
    for d in adb.device_list():
        device = android_boy.AndroidBoy(d.serial, (240, 160))
        boy_list.append(device)