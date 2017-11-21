import os, sys
import falcon
from wsgiref import simple_server
import logging, time
from utilities.caching import *
from modules import *


api = falcon.API()

#Initializing processing
cache = CacheLineResults()


class DocServe(object):

    def on_get(self, req, resp, line=None):
        '''

        :param req: Request object
        :param resp: Response class
        :return: response line
        '''

        # Get parameters

        # Process Inputs - Refactored in event of expanded input processing ( extra params )
        line = ProcessInputs.processOneLine(line)

        # File name
        filename = os.path.abspath('%s' % sys.argv[1])
        print filename


        
        # Check if result in cache and return, else process (+/-1)

        if line in cache.showStash():
            final_result = cache.retrieve(line)
            resp.status = falcon.HTTP_200


        else:
            processStart = ProcessFile()
            #Invoke processing
            try:

                line_content = processStart.getLine(filename,line)

                cache.storeIt(line, line_content)
                final_result = line_content
                resp.status = falcon.HTTP_200
            except Exception, e:
                resp.status = falcon.HTTP_413
                resp.body = falcon.HTTP_413
                raise Exception(e)


            #Secondary cache
            line = int(line)
            cache.storeIt(line-1,processStart.getLine(filename,line-1))
            cache.storeIt(line+1,processStart.getLine(filename,line+1))

        #Return result
        resp.body = final_result
        resp.set_header('Powered-By', 'Line Serve API')


    def on_post(self,req,resp): pass

    def on_delete(self,req,resp): pass

    def on_put(self,req,resp): pass


api.add_route('/lines/{line}', DocServe())


if __name__ == '__main__':

    filename = str(sys.argv[1])
    httpd = simple_server.make_server(host='localhost', port=8890,app=api)
    print 'Serving on: http://%s:%s/test/' % ('localhost',8890)
    httpd.serve_forever()
    # os.system('redis-server')


