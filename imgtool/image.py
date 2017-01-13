# coding: utf-8
from PIL import Image,ImageDraw,ImageFont
from util import ReadExcel

url = 'testImage/'
Font1 = ImageFont.truetype('song.ttf',24,index=0,encoding='utf-8')
#set the image width,height
excelList = ReadExcel.excel_sheet_byIndex('C:\\Users\\Administrator\\Desktop\\Image.xlsx' , 0)
for i in range(0,len(excelList)):
    width = int(excelList[i][2])
    height = int(excelList[i][3])
    adName = excelList[i][0]
    adCode = excelList[i][1]
    newImage = Image.new("RGBA", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(newImage)
    draw.text((10, 10), adName+adCode, fill=(255, 0, 0), font=Font1)
    draw.line(((0, height), (width, height), (width, 0), (0, 0), (0, height)), fill=(0, 0, 0), width=10)
    imageName = adName + adCode
    print imageName
    newImage.save(url + imageName+'.png','png')


