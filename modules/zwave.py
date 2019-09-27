from modules.device import device 
from modules.logger import logger

class zwave(logger):
    home_id = ""
    node_id = ""
    chip_version = 0.0
    protocol_verison = ""
    pid = "" # 제품아이디
    def __init__(self, home_id, node_id, chip, protocol, pid = None):
        logger.__init__(self, "zwave")

        self.home_id = home_id
        self.node_id = node_id
        self.chip_version = chip
        self.protocol_verison = protocol


def searchZwave():
    zwave_lst = list()
    '''
    무선랜 탐색하여 zwave_lst에 zwave 객체 추가
    '''

    for zw in zwave_lst:
        zw.log.info("Searched z-wave, home_id: " + zw.home_id +
                    ", node_id: " + zw.node_id + 
                    ", version: " + zw.version)
    return zwave_lst 


'''
@params: zwave 객체
@return: True or False 
'''

def zwaveVersionCheck(zw):

    pass      


if __name__ == "__main__":
    zw = zwave("111","222",1.2,"fuck")