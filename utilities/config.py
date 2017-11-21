import ConfigParser
import os


class interfaceConfig(object):
    CONFIG_FILE_PATH = "config.ini"
    '''
    Future improvements: Can be easily replaced by Zookeeper or 
    larger scalable config server
    '''

    def __init__(self):
        try:
            configFileName = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', self.CONFIG_FILE_PATH))
            parser = ConfigParser.SafeConfigParser()
            parser.read(configFileName)
        except Exception, e:
            raise Exception('Unable to read configuration file')

        self.parser = parser

        # DEV
        self.host = parser.get('development', 'host')
        self.port = parser.get('development', 'port')

        # PRE - PROCESS

        self.files_per_folder = get('pre-processing', 'files_in_folder')
        self.lines_per_file = get('pre-processing', 'lines_in_file')


        # STG
        self.chost = parser.get('staging', 'host')
        self.cport = parser.get('staging', 'port')


        # PROD
        self.qhost = parser.get('production', 'host')
        self.qport = parser.get('production', 'port')

        #Logging
        self.formatter = parser.get('logging','')

if __name__ == '__main__':
    config = ConfigParser()

