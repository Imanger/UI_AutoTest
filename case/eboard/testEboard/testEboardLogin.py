# -*- coding: utf-8 -*-
import comm.location as lo
from selenium import webdriver
from comm import Log
from comm import common
import unittest
import time
import paramunittest

#从excle中获取登录密码，记录日志
eboardLogin_xls = common.get_xls("eboard","do","eboardLogin.xls","login")
log = Log.Log()
logger = log.get_logger()

@paramunittest.parametrized(*eboardLogin_xls)
class EboardLogin(unittest.TestCase):
    def setParameters(self,case_name,loginName,password,result):
        self.case_name = case_name
        self.loginName = loginName
        self.password = password
        self.result = result


    def setUp(self):
        logger.info(u"开始执行：%s"%self.__class__.__name__)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.class_name = self.__class__.__name__

    def testEboardLogin(self):
        # global login
        try:
            login = lo.eboardLogin(self.driver,self.loginName,self.password)
            time.sleep(2)
            logger.info(u'开始断言：%s'%self.class_name)
            self.check_result()
        except Exception as msg:
            logger.info(u"异常原因：%s"%msg)
            log.get_screen(self.driver,self.class_name)
            raise

    def check_result(self):
        if self.result == '班牌登录成功':
            value = lo.findByXpath(self.driver,'//span[@class="title--2VNQzgL305AvwxKV5Fceee"]').text
            time.sleep(2)
            self.assertEqual(value,'本周红花榜')
        if self.result == '未输入班牌编号':
            value = lo.findByXpath(self.driver, '//div[@class="ant-message-custom-content ant-message-error"]').text
            self.assertEqual(value,'请输入班牌编号')
        if self.result == '密码错误':
            value = lo.findByXpath(self.driver, '//div[@class="ant-message-custom-content ant-message-error"]').text
            self.assertEqual(value,'登入密码输入错误')
        if self.result == '登入编号未创建':
            value = lo.findByXpath(self.driver, '//div[@class="ant-message-custom-content ant-message-error"]').text
            self.assertEqual(value,'登入编号未创建')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()