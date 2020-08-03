# -*- coding: utf-8 -*-
import comm.location as lo
from selenium import webdriver
from comm import Log
from comm import common
import unittest
import time
import paramunittest

#从excle中获取登录密码，记录日志
eboardLogin_xls = common.get_xls("eboard","do","eboardLogin.xls","report")
log = Log.Log()
logger = log.get_logger()

@paramunittest.parametrized(*eboardLogin_xls)
class EboardReport(unittest.TestCase):
    def setParameters(self,case_name,result):
        self.case_name = case_name
        self.result = result


    def setUp(self):
        logger.info(u"开始执行：%s"%self.__class__.__name__)
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.class_name = self.__class__.__name__

    def testEboardReport(self):
        try:
            lo.eboardReport(driver,987654,987654)
            time.sleep(2)
            logger.info(u'开始断言：%s' % self.class_name)
            self.check_result()
        except Exception as msg:
            logger.info(u"异常原因：%s" % msg)
            log.get_screen(driver, self.class_name)
            raise

    def check_result(self):
        if self.result == '存在报告':
            value = lo.findByXpath(driver,'//div[@class="titleBar--1NEq7FZ0XDcmTAb8kO0sAr"]').text
            time.sleep(2)
            self.assertEqual(value,'成绩概览')

    def tearDown(self):
        driver.quit()
if __name__ == '__main__':
    unittest.main()