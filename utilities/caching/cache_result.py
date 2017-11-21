# from redis_cache import RedisConnect, cache_it, SimpleCache
import redis
import logging


class CacheLineResults(object):
    '''
    Simple Redis cache for close to 10000 keys. Scale to private server if need be
    '''

    def __init__(self):
        #Only Invoke a separate Cache server once bites exceed (N)
        self.rCache = redis.StrictRedis(host='localhost', port=6379, db=0)
        # self.rCache = SimpleCache(limit=10000,expire=None)


    def storeIt(self,line,result):
        if line not in self.rCache.keys():
            self.rCache.set(line,result)
        else:
            logging.debug('Cache: %s already present in store' % line)

    def retrieve(self,line):
        return self.rCache.get(line)


    def showStash(self):
        return self.rCache.keys()
