# encoding=utf8
import sys
import json
import urlparse
from util import ReadExcel, HttpRequestHandle
from ody import CommonUse
from Handle import LogInOut

#setCode
reload(sys)
sys.setdefaultencoding('utf-8')

#login
_cookies = LogInOut.login('superadmin', '123456')

#insertAdLocation
adLocationUrlPath='ad-whale-web/adBase/addAdPosition.do'
adLocationUrl=urlparse.urljoin(CommonUse.BACKBASEURL, adLocationUrlPath)
excelList = ReadExcel.excel_sheet_byIndex('C:\\Users\\Administrator\\Desktop\\AddAdLocation.xlsx' , 0)
for i in range(0,len(excelList)):
    adLocation={"name": excelList[i][0], "isEnabled": 'true',"pageType":excelList[i][1],"code": excelList[i][2],"sourceSizeLimit":excelList[i][3],"systemId":1,"companyId":CommonUse.COMPANYID,"platform":excelList[i][4],"version":0,"createBy":10000000,"type":"0,1,2","height":768,"width":1366,"imageMaxSize":500}
    adLocationResult = HttpRequestHandle.requestPost_cookies(adLocationUrl, json.dumps(adLocation),CommonUse.HEAD, _cookies)
    print adLocationResult.text

#logout
print(LogInOut.logout())