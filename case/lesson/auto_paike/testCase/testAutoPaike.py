# -*- coding: utf-8 -*-
from selenium import webdriver
import comm.location as lo
import comm.element as el
import unittest
import paramunittest
import random
from comm import Log
from comm import common
from selenium.webdriver.support.ui import Select #下拉选择元素
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.by as By
import time
import datetime
from pymouse import PyMouse
from pykeyboard import  PyKeyboard
import os
from urllib import request
from urllib import parse
import ssl
import json
import urllib.request
from comm import getHTMLResponse as RS


CreateAutoPaike_xls = common.get_xls("lesson","auto_paike","lekeLogin.xls","login")
log = Log.Log()
logger = log.get_logger()
#ssl取消全局验证
ssl._create_default_https_context = ssl._create_unverified_context


@paramunittest.parametrized(*CreateAutoPaike_xls)
class AutoPaike(unittest.TestCase):
    def setParameters(self,case_name,loginName,password,result):
        self.case_name = str(case_name)
        self.loginName = str(loginName)
        self.password = str(password)
        self.result = str(result)

    def setUp(self):
        logger.info(u'开始执行：%s'%self.__class__.__name__)
        global webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.class_name = self.__class__.__name__

    def testShouKe(self):
        try:
            login = lo.login(self.driver,self.loginName,self.password)
            time.sleep(0.5)
            element=lo.findByXpath(self.driver,'//li[@class="c-teachingapllication__typeeight"]')
            element.click()
            self.driver.implicitly_wait(10)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            #新建排课任务
            # lo.findByXpath(self.driver,'//div[@class="right"]').click()
            #切换弹窗
            # WebDriverWait(self.driver,10).until(EC.alert_is_present())
            # alert =self.driver.switch_to_alert()`
            # current_time = datetime.datetime.now()
            # day_time=current_time.strftime('%m%d %H:%M')
            # lo.findByXpath(self.driver,'//div[@class="wrap"]/div[1]/form/div/ul/li/input').send_keys("自动化排课%s"%day_time)
            # time.sleep(0.5)
            # lo.findByXpath(self.driver,'//button[@class="btn-base btn-green"]').click()
            # self.driver.implicitly_wait(10)
            # 编辑排课
            lo.findByXpath(self.driver,'//tbody[@id="jBody"]/tr[1]/td[5]/a[1]').click()
            # 基础设置下一步
            element=lo.findByXpath(self.driver,'//input[@id="jNext"]')
            element.click()
            self.driver.implicitly_wait(10)
            # #导入新增授课计划
            # Import = lo.findByXpath(self.driver,'//button[@class="u-btn-hollow___1osUN u-btn___1RHja import-btn___3Ly8P"]')
            # Import.click()
            # #行政班导入
            # time.sleep(0.5)
            # upload = lo.findByXpath(self.driver,'//button[@class="ant-btn upload-btn___2ooDW"]')
            # upload.click()
            # time.sleep(0.5)
            # #获取上传路径
            # proDir = os.path.abspath(os.path.join(os.getcwd()))
            # fileDir = os.path.join(proDir, 'file\\lesson\\auto_paike\\upload行政班.exe')
            # os.system(fileDir)
            # time.sleep(0.5)
            # lo.findByXpath(self.driver,'//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            # time.sleep(0.5)
            # #走班导入
            # Import = lo.findByXpath(self.driver,'//button[@class="u-btn-hollow___1osUN u-btn___1RHja import-btn___3Ly8P"]')
            # Import.click()
            # #切换到走班页签
            # lo.findByXpath(self.driver,'//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div[1]/div[2]').click()
            # time.sleep(1)
            # upload = lo.findByXpath(self.driver,'//div[@class="ant-tabs-content ant-tabs-content-animated"]/div[2]/descendant::button[@class="ant-btn upload-btn___2ooDW"]')
            # upload.click()
            # time.sleep(0.5)
            # #获取上传路径
            # proDir = os.path.abspath(os.path.join(os.getcwd()))
            # fileDir = os.path.join(proDir, 'file\\lesson\\auto_paike\\upload走班.exe')
            # os.system(fileDir)
            # time.sleep(0.5)
            # #保存导入
            # lo.findByXpath(self.driver, '//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            # time.sleep(0.5)
            # #选修班导入
            # Import = lo.findByXpath(self.driver,'//button[@class="u-btn-hollow___1osUN u-btn___1RHja import-btn___3Ly8P"]')
            # Import.click()
            # # 切换到选修班页签
            # lo.findByXpath(self.driver, '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div[1]/div[3]').click()
            # time.sleep(1)
            # upload = lo.findByXpath(self.driver,'//div[@class="ant-tabs-content ant-tabs-content-animated"]/div[3]/descendant::button[@class="ant-btn upload-btn___2ooDW"]')
            # upload.click()
            # time.sleep(0.5)
            # #获取上传路径
            # proDir = os.path.abspath(os.path.join(os.getcwd()))
            # fileDir = os.path.join(proDir, 'file\\lesson\\auto_paike\\upload选修班.exe')
            # os.system(fileDir)
            # time.sleep(0.5)
            # # 保存导入
            # lo.findByXpath(self.driver, '//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            # time.sleep(2)

            #单个添加授课计划
            lo.findByXpath(self.driver,'//button[@class="u-btn-hollow___1osUN u-btn___1RHja singleAdd-btn___3D8fz"]').click()
            time.sleep(1)
            #选择年级
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/descendant::span[@class="c_input_title___1vADM"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___O2imj c-select-result c-select-result_active___3zBP-"]/li[contains(text(),"高一")]').click()
            time.sleep(0.5)
            #选择班级属性-行政班
            lo.findByXpath(self.driver, '//div[@class="teach-plan-box___1eL_V"]/div[2]/ul/li[1]/descendant::span[@class="c_input_title___1vADM"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___O2imj c-select-result c-select-result_active___3zBP-"]/li[contains(text(),"行政班")]').click()
            time.sleep(0.5)
            #选择班级名称0
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/div[1]/ul/li[2]/descendant::span[@class="c_input_title___1vADM"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___O2imj c-select-result c-select-result_active___3zBP-"]/li[2]').click()
            time.sleep(0.5)
            #选择学科
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/div[2]/ul/li[2]/descendant::span[@class="c_input_title___1vADM"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___O2imj c-select-result c-select-result_active___3zBP-"]/li[2]').click()
            time.sleep(0.5)
            #选择老师
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/div[1]/ul/li[3]/descendant::input[@class="c-input___1Rua- c-input"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___3Qhft c-select-result_active___12Frm c-select-result"]/li[1]').click()
            time.sleep(0.5)
            #选择周课时
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/div[2]/ul/li[3]/descendant::span[@class="c_input_title___1vADM"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___O2imj c-select-result c-select-result_active___3zBP-"]/li[2]').click()
            time.sleep(0.5)
            #选择教学场地
            lo.findByXpath(self.driver,'//div[@class="teach-plan-box___1eL_V"]/div[2]/ul/li[4]/descendant::input[@class="c-input___1Rua- c-input"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//ul[@class="c-select-result___3Qhft c-select-result_active___12Frm c-select-result"]/li[1]').click()
            time.sleep(0.5)
            #保存
            lo.findByXpath(self.driver,'//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            time.sleep(2)

            #批量设置课时数
            lo.findByXpath(self.driver,'//input[@class="ant-checkbox-input"]').click()
            lo.findByXpath(self.driver,'//button[@class="u-btn-hollow___1osUN u-btn___1RHja setClazzNum-btn___MTCOi"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//div[@class="setClazzNum___2aHVT"]/p[1]/input[@class="u-ipt-sm___2u2wH"]').send_keys(10)
            lo.findByXpath(self.driver,'//div[@class="setClazzNum___2aHVT"]/p[2]/input[@class="u-ipt-sm___2u2wH"]').send_keys(1)
            lo.findByXpath(self.driver,'//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            time.sleep(1)
            #下一步规则设置
            lo.findByXpath(self.driver,'//button[@class="u-btn-bg-turquoise___e_Hc0 u-btn___1RHja nextStep-btn___37iZ6"]').click()
            time.sleep(0.5)
            lo.findByXpath(self.driver,'//button[@class="btn-ok btn-ok___2kFDA btn___3cb76"]').click()
            #下一步手工预排
            self.driver.implicitly_wait(10)
            lo.findByXpath(self.driver,'//input[@id="jNext"]').click()
            time.sleep(1)

            #获取课程数据
            url=self.driver.current_url
            #获取cookie
            cookie_list = self.driver.get_cookies()
            cookie_str = ""
            # 组装cookie字符串
            for item_cookie in cookie_list:
                item_str = item_cookie["name"] + "=" + item_cookie["value"] + "; "
                cookie_str += item_str

            params = (url.split('?')[1]).split('&')
            params_dict = dict([s.split('=') for s in params])
            #获取授课计划值
            teachPlan=RS.requestHtml(params_dict,cookie_str)
            subName=[]
            weekCnt=[]
            for m in teachPlan:
                for n in m:
                    subName.append(n.get('subName'))
                    weekCnt.append(n.get('weekCnt'))

            for i in range(10):
                lo.findByXpath(self.driver,'//tr[@id="tr_1_1"]/td['+str(i+3)+']').click()
                time.sleep(22)












        except Exception as msg:
            logger.info(u"异常原因：%s" % msg)
            log.get_screen(self.driver, self.class_name)
            raise

