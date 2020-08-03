# -*- coding: utf-8 -*-
import os
import readConfig
from xlrd import open_workbook
from selenium import webdriver
from comm import location as lo
import time


localReadConfig = readConfig.ReadConfig()

def open_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def close_browser(browser):
    browser.close()


def open_url(section,param):
    '''
    open web page by url
    :param name:
    :return:
    '''
    url = localReadConfig.get_webServer(section,param)  #获取本地配置文件中的浏览器数据
    print(url)
    browser = open_browser()
    browser.get(url)
    return browser

def get_xls(web,site,xls_name,sheet_name):
    # web = runSet.get_web()
    # site = runSet.get_site()

    cls = []
    # get  excel file path
    xls_path = os.path.join(readConfig.proDir,'file',web,site,xls_name)
    print("xls路径："+xls_path)

    #open excel file
    book = open_workbook(xls_path)
    #get sheet by name
    sheet = book.sheet_by_name(sheet_name)
    #get nrows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
            print('excle用例:'+str(sheet.row_values(i)))#表记录是一个list，转化成str再拼接打印

    return cls





