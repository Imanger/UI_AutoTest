# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from comm import location as lo
import unittest
from selenium import webdriver
import time
import os

# driver = webdriver.Chrome()
# driver.maximize_window()

def demo():
    proDir = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
    proDir = os.path.abspath(os.path.join(os.getcwd(), "../../../.."))
    fileDir = os.path.join(proDir,'file\\lesson\\auto_paike\\upload行政班.exe')
    configPath = os.path.join(proDir,'config.ini').replace("\\","/")#y以上目录，组合成新目录
    print(proDir)
    print(fileDir)

    # url = "https://lesson.leke.cn/auth/provost/paike/manage/setBase.htm?paikeTaskId=2706&spm=104057"
    # lo.login(driver,883318,'lekecn666')
    # time.sleep(1)
    # driver.get(url)

demo()


