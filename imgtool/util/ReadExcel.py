#-*- coding: utf-8 -*-
import sys
import xlrd

#setCode
reload(sys)
sys.setdefaultencoding('utf-8')

def open_excel(excelFile):
    try:
        #open a workbook
        workbook=xlrd.open_workbook(excelFile)
        print 'read file is ok'
        return workbook

    except Exception,e:
        return str(e)
#根据索引获取excel表格中的数据
def excel_sheet_byIndex(excelFile, by_index):
    wookbook = open_excel(excelFile)
    sheet = wookbook.sheets()[by_index]
    rowsCount = sheet.nrows
    # colsCount = sheet.ncols
    sheetList = []
    for rowNum in range(1,rowsCount):
        rowData = sheet.row_values(rowNum)
        sheetList.append(rowData)
    return sheetList


