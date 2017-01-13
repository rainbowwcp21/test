import requests

def requestPostUrl(url):
    requestResult = requests.post(url)
    return requestResult

def requestPostHeader(url,data,header):
    requestResult = requests.post(url,data=data,headers=header)
    return requestResult

#need cookies
def requestPost_cookies(url,data,header,cookies):
    requestResult = requests.post(url,data=data,headers=header,cookies=cookies)
    return requestResult