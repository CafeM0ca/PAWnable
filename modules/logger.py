import logging
import logging.handlers
import os

class logger:
    #로그 관련 멤버변수
    log = logging.getLogger("data logger")
    fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    file_handler = None 
    stream_handler = logging.StreamHandler()
    

    def __init__(self, log_file):
        p = os.getcwd()
        print(p)
        self.file_handler = logging.FileHandler(p + '/log/' + log_file)
        self.log.setLevel(logging.INFO)
        self.file_handler.setFormatter(self.fomatter)
        self.stream_handler.setFormatter(self.fomatter)
        self.log.addHandler(self.file_handler)
        self.log.addHandler(self.stream_handler)