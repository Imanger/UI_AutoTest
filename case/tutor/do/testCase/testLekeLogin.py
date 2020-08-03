# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from comm import location as lo
from time import sleep
from selenium import webdriver
import unittest
import paramunittest
from comm import common
from comm import Log
import HTMLTestReportCN

#为实现不同路径的测试用例，excle路径由业务方传入
lekeLogin_xls = common.get_xls("tutor","do","lekeLogin.xls","login")    #web,site,xls_name,sheet_name
log = Log.Log()
logger = log.get_logger()

@paramunittest.parametrized(*lekeLogin_xls) #参数化用例
class LekeLogin(unittest.TestCase):
    def setParameters(self,case_name,LoginName,password,result):
        self.case_name = str(case_name)
        self.LoginName = str(int(LoginName))
        self.password = str(password)
        self.result = str(result)

    def setUp(self):
        logger.info(u"开始执行: %s"%self.__class__.__name__)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.clss_name = self.__class__.__name__+'_'+self.result    #名称更具有目的性

    def testLekeLogin(self):
        try:
            lo.login(self.driver,self.LoginName,self.password)  #使用账号密码登录
            sleep(2)
            logger.info(u"我要断言了：%s"%self.clss_name)
            self.check_result() #进行断言
        except Exception as msg:
            logger.info(u"异常原因：%s"%msg)
            log.get_screen(self.driver,self.clss_name)
            raise #再抛异常

    def check_result(self):
        if self.result == '学生登录成功':
            value = lo.findByXpath(self.driver,'/html/body/div[6]/div/div[2]/div[2]/div[1]/header').text
            sleep(2)
            self.assertEqual(value,'我的成长树')
        if self.result == '乐号不存在':
            value = lo.findByXpath(self.driver,'//*[@id="err_placeholder"]').text
            self.assertEqual(value,'该用户不存在')
        if  self.result == '密码错误':
            value = lo.findByXpath(self.driver,'//*[@id="err_placeholder"]').text
            self.assertEqual(value,'密码不正确')
        if self.result == '禁用':
            value = lo.findByXpath(self.driver,'//*[@id="err_placeholder"]').text
            self.assertEqual(value,'该账号未激活')

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
