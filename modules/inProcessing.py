import os
import multiprocessing as mp
import falcon

class ProcessInputs(object):

    @staticmethod
    def processOneLine(line):

        try:
            if line is not None:
                line = int(line)
        except:
            pass

        return line


class ProcessFile(object):

    def __init__(self):
        pass


    def getLine(self,file,line):
        '''
        Takes in line number to return contents of the line
        :param line:
        :return: returns contents of the file before line end
        '''

        try:
            # file = './mockData/file_1_50.txt'
            result = self.threadUp(file,line)

            if line >= 50:
                raise Exception(falcon.HTTP_413)

        except Exception ,e:
            raise Exception('Error : %s' % e)

        return result

    def process_wrapper(self, chunkStart, chunkSize, line, file):
        '''
        Opens chunk, reads specific line and checks for line number
        :param chunkStart:
        :param chunkSize:
        :param line:
        :param file:
        :return:
        '''
        with open(file, 'rb') as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()
            for l in lines:
                if '%s.' % line in l:
                    return l

    def chunkify(self, fname, size=1024 * 1024):
        '''
        Breaks file into smaller chunker and usese seek function to directly access
        the line and read it into memory for processing

        :param fname:
        :param size:
        :return:
        '''
        fileEnd = os.path.getsize(fname)
        with open(fname, 'r') as f:
            chunkEnd = f.tell()
            while True:
                chunkStart = chunkEnd
                f.seek(size, 1)
                f.readline()
                chunkEnd = f.tell()
                yield chunkStart, chunkEnd - chunkStart
                if chunkEnd > fileEnd:
                    break

    def threadUp(self, file, line):
        '''
        Uses multiprocessing to pool all process wrappers
        :param file:
        :param line:
        :return:
        '''
        # Initialize pools
        pool = mp.Pool(8)
        temp_job_queue = []

        # create jobs
        for chunkStart, chunkSize in self.chunkify(file):
            temp_job_queue.append(pool.apply_async(self.process_wrapper, (chunkStart, chunkSize, line, file)))

        # wait for all jobs to finish
        for job in temp_job_queue:
            completed_task = job.get()

        # clean up pools after use
        pool.close()

        return completed_task




