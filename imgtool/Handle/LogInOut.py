from ody import CommonUse
import urlparse
from util import HttpRequestHandle
import json

def login(username,password):
    loginUrlPath = 'ouser-web/mobileLogin/login.do'
    loginUrl = urlparse.urljoin(CommonUse.BACKBASEURL, loginUrlPath)
    loginMessage = {'username': username, 'password': password, 'type': 1}
    loginResult = HttpRequestHandle.requestPostHeader(loginUrl,json.dumps(loginMessage),CommonUse.HEAD)
    _cookies = loginResult.cookies
    print "login success"
    return _cookies

def logout():
    logoutUrlPath = 'ouser-web/mobileLogin/exit.do'
    logoutUrl = urlparse.urljoin(CommonUse.BACKBASEURL, logoutUrlPath)
    logoutMessage = HttpRequestHandle.requestPostUrl(logoutUrl)
    print "logout successful"
    return logoutMessage