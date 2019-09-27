#-*- coding:utf-8 -*-
import time
from modules.wifi import *
from modules.bluetooth import *
from modules.zwave import *
from modules.logger import *

class core(logger):
    wifi_lst = None
    bluetooth_lst = None
    zwave_lst = None
    def __init__(self):
        
        logger.__init__(self, "core")
        # 아스키 아트

        for i in range(0, 60):
            print('*', end="")
            time.sleep(0.2)

        print("")
        self.log.info("Load WIFI LIST")
        self.wifi_lst = searchWifi()

        for i in range(0, 60):
            print('*', end="")
            time.sleep(0.2)

        print("")
        self.log.info("Load BLUETOOTH LIST")
        self.bluetooth_lst = searchBluetooth()

        for i in range(0, 60):
            print('*', end="")
            time.sleep(0.2)

        print("")
        self.log.info("Load Z-WAVE LIST")
        self.zwave_lst = searchZwave()



    # wifi list에서 하나씩 뽑아서 취약점 체크함 
    def testWifi(self):
        self.log.info("WIFI Vulnrable Checking")
        cnt = 0
        can_exploit = False
        for wf in self.wifi_lst:
            can_exploit = checkWifiVuln(wf)
            if can_exploit:
                self.log.info("Fail")
            else:
                cnt+=1
                self.log.info("PASS")

        print("(" + str(cnt) + "/" + len(self.wifi_lst) + ") PASS")

    # bluetooth list에서 하나씩 뽑아서 버전 체크함 
    def testBluetooth(self):
        self.log.info("BLUETOOTH Version Checking")
        cnt = 0
        can_exploit = False
        for bt in self.bluetooth_lst:
            can_exploit = bluetoothVersionCheck(bt)
            if can_exploit:
                self.log.info("Fail")
            else:
                cnt+=1
                self.log.info("PASS")

        print("(" + str(cnt) + "/" + len(self.bluetooth_lst) + ") PASS")
    
    # zwave list에서 하나씩 뽑아서 버전 체크함 
    def testZwave(self):
        self.log.info("Z-WAVE Version Checking")
        cnt = 0
        can_exploit = False
        for zw in self.zwave_lst:
            can_exploit = zwaveVersionCheck(zw)
            if can_exploit:
                self.log.info("Fail")
            else:
                cnt+=1
                self.log.info("PASS")

        print("(" + str(cnt) + "/" + len(self.zwave_lst) + ") PASS")
 

if __name__ == "__main__":
    c = core()