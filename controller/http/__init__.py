http_codes = {
                200:'Ok',
                201:'Created',
                204:'No content',
                301:'Moved permanently',
                307:'Temporary Redirect',
                308:'Permanent Redirect ',
                400:'Bad Request',
                401:'Unauthorized',
                403:'Forbidden',
                404:'Not Found',
                405:'Method Not Allowed',
                406:'Not Acceptable',
                409:'Conflict',
                429:'Too many requests',
                500:'Internal server error',
                501:'Not Implemented',
                502:'Bad Gateway',
                503:'Service Unavailable'
             }

class HTTP_RESPONSE:
    def __init__(self,statusCode):
        self.status_code = statusCode
    
    def returnMessage(self,response):
        response.status_code = self.status_code
        return http_codes[self.status_code] if self.status_code in http_codes else 'undefined status code'
    
    def returnCustomMessage(self,response,cMessage):
        response.status_code = self.status_code
        return cMessage
    
    def returnErrorMessage(self,response,err):
        response.status_code = self.status_code
        return {
            "message" : err
        }
    
        