
import logging
# from config import *

class Logging(object):
    '''
    Future work - Gather all configurations from main config file
    '''

    def __init__(self):
        self.logger = logging.getLogger()
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.CRITICAL)


    def logfileStorage(self,medium):

        '''
        Store logs to a log file or log server (logz.io or Data dog)
        :param medium:
        :return:
        '''
        pass