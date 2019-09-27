from modules.device import device 
from modules.logger import logger
# protocol 상속
class wifi(device, logger):
    bss_id = ""
    ss_id = "" 
    ess_id = "" 
    def __init__(self, bss_id, ss_id, ess_id, ip, id = None):
        # wifi 객체들을 취약점 검사한 로그
        logger.__init__(self, "wifi")

        # device는 packet 로그
        device.__init__(self, "wifi", ip, id)

        self.bss_id = bss_id
        self.ss_id = ss_id
        self.ess_id = ess_id

def searchWifi():
    wifi_lst = list()
    '''
    무선랜 탐색하여 wifi_lst에 sifi 객체 추가
    '''

    for w in wifi_lst:
        w.log.info("Searched wifi bss_id : " + w.bss_id + 
                    ", ss_id: " + w.ss_id + 
                    ", ess_id: " + w.ess_id)     
    return wifi_lst 



'''
bss_id, ss_id, ess_id를 바탕으로 취약점에 뚫리는지 안뚫리는지 체크함
@params: wifi 객체
@return: True or False
'''
def checkWifiVuln(wf):
    exploit_possible = False # exploit 가능 여부

    '''
    취약점 판단 로직
    '''

    wf.log.info("Protocol: wifi, bss_id: " + wf.bss_id + 
                 ", ss_id: " + wf.ss_id + ", ess_id: " + wf.ess_id +
                 ", exploit_possible: " + str(exploit_possible))
    return exploit_possible

if __name__ == "__main__":
    w = wifi("1234","1234","1234","123.222.112.113")