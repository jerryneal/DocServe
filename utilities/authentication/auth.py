import falcon

class AuthLibarary(object):
    '''
    Future work but very necessary
    '''

    def authenticate_request(self, req, resp):
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')
        if token is None:
            raise falcon.HTTPUnauthorized('Auth token required')
        if not self.isvalid(token, account_id):
            raise falcon.HTTPUnauthorized('Authentication required')

    def isValid(self, token, account_id):
        '''
        Future work - either with database or whatever data store is available
        :param token:
        :param account_id:
        :return:
        '''
        return True


    def rateLimieter(self,token,accountId):
        '''
        Ensures one API user does not throttle down the system
        :param token:
        :param accountId:
        :return:
        '''
        pass

