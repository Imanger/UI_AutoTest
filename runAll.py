# -*- coding: utf-8 -*-
from comm.Log import MyLog as Log
import HTMLTestReportCN
import readConfig as readConfig
import time
import comm.runSet as runRet
from comm import sendEmail as email

localReadConfig = readConfig.ReadConfig()

class AlllTest():
    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.resultPath = self.log.get_report_path()

    def run(self):
        suite = runRet.set_suite() #得到需要执行的用例的suite

        try:
            if suite is not None:
                self.logger.info(u'****************TEST START*********************')
                time.sleep(1)
                print(u'报告路径：'+self.resultPath)
                fb = open(self.resultPath,'wb')
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fb,title = u'乐课网UI自动化',tester='zhiying.liu')
                self.logger.info(u'执行case')
                runner.run(suite)
                fb.close()
            else:
                self.logger.info(u'没有可执行用例!')
                print(u'没有可执行用例！')

        except Exception as e:
            self.logger.error(str(e))
            print(str(e))
        finally:
            self.logger.info(u'****************TEST END*********************')

    def send_email(self):
        email.send_email(self.resultPath)

if __name__ ==  "__main__":
    alltest = AlllTest()
    alltest.run()
    # alltest.send_email()