#-*- coding:utf-8 -*-
from modules.device import device 
from modules.logger import logger

class bluetooth(device, logger):
    # bluetooth 버전
    version = 0.0 
    def __init__(self, ip, version, id = None):
        # bluetooth 객체들을 취약점 검사한 로그
        logger.__init__(self, "bluetooth")
        # device는 packet 로그
        device.__init__(self, "bluetooth", ip, id)

        self.version = version

'''
블루투스 장비 리스트를 탐색하여 리스트로 반환
@return : list() 
'''
def searchBluetooth():
    bt_lst = list()
    '''
    sniffing 하여 bt_lst에 bluetooth 객체 추가
    '''

    for bt in bt_lst:

        bt.log.info("Searched bluetooth device ip : " + bt.ip + 
                    ", version : " + bt.version)    
    return bt_lst



'''
파라미터 : 대상 모듈의 정보.
내부 로직 : 모듈 개발자가 알아서 짜세요!
반환값 : 취약점 존재 여부 -true false 
종류 정보 위험성
'''

'''
@param : 블루투스 객체
@logic : 버전에 따라서 발생하는 취약점을 체크하고 반환값을 설정
            블루투스 객체, 블루투스 버전, 취약점 종류, 위험성 json 객체로 반환
            위험성은  0~3단계. 초록색->빨간색
@return : exploit 가능여부
'''
def bluetoothVersionCheck(bt):
    can_exploit = False
    version = bt.version
    vuln_type = "" 
    dangerous_level = "" 

    # 취약점 체크 로직 수행

    # log에 기록
    bt.log.info("Protocol: bluetooth, " + 
                "version: " + version + 
                ", vuln_type: " + vuln_type +
                ", dangerous_level: " + dangerous_level)

    return can_exploit

if __name__ == "__main__":
    bt = bluetooth("123.221.131.111",3.3)