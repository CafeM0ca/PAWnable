#-*- coding:utf-8 -*-
# z-wave device 구조체 파일 
from modules.logger import *

# src와 dst의 protocol은 같아야 한다.
class packet:
    src = None
    dst = None
    data = None
    # 거쳐간 slave route 리스트 멤버변수 필요
    # 거쳐간 router slave route 리스트에 추가하는 함수 필요
    # slave route 거쳐간 로그 보여주는 함수
    def __init__(self, src, dst, data):
        if src.getProtocol() != dst.getProtocol():
            self.__del__()
            return
        self.src = src
        self.dst = dst
        self.data = data

    def getSrc(self):
        return self.src
    def getDst(self):
        return self.dst
    def getData(self):
        return self.data


# 제공하는 프로토콜은 3종류, wifi, bluetooth, z-wave. 
# 우선 헤더 뜯어보는 작업들은 생략.
class device(logger): 
    protocol = None
    id = None
    ip = None
    ################################################
    def __init__(self, prot, ip, id = None, log_file="packet"):
        logger.__init__(self, log_file)
        self.protocol = prot 
        self.ip = ip
        self.id = id

        self.log.setLevel(logging.INFO)
        self.file_handler.setFormatter(self.fomatter)
        self.stream_handler.setFormatter(self.fomatter)
        self.log.addHandler(self.file_handler)
        self.log.addHandler(self.stream_handler)
        self.log.info("Protocol : " +  prot + ", IP: " + ip + " found")


    def getProtocol(self):
        return self.protocol

    # 패킷 보내는 함수
    # dst : 받는 디바이스 객체
    # data : 보낼 값
    def sendPacket(self, dst, data):
        if self.getProtocol() != dst.getProtocol() :
            self.log.error("Error, Protocol is not same. Fail to sending packet")
        self.log.info("src ip: " + self.ip + " send packet to dst ip: " + dst.ip + ". data: " + data)
        dst.receivePacket(self.ip, data)

    # 패킷 받는 함수. 별도로 호출될 일은 없음. 보내는 쪽에서 호출함
    # src : 보내는 객체 ip
    # data : 받는 값
    def receivePacket(self, src, data):
        self.log.info(self.ip + " receive packet from src ip: " + src + ". data: " + data)

    # 보낸 정보, 받은 정보, 보낸 데이터, 받은 데이터가 필요.
    # 주고 받은 데이터 로그 리스트 필요
    # 데이터 로그 리스트 보여주는 함수 필요

if __name__ == "__main__":
    d1 = device("wifi", "112.113.111.131", "GS-123")
    d2 = device("wifi", "122.123.131.231", "GS-456") 
    d3 = device("z-wave", "212.123.211.132","ZS-456") 
    d1.sendPacket(d2, "test1")
    d2.sendPacket(d3, "test2")