#coding = 'utf-8'
#-*- coding: UTF-8 -*-

from selenium import webdriver
import time

values={'search','webdriver',u'虫师'}

for search in values:
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()
