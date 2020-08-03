# -*- coding: utf-8 -*-
import unittest
from comm import common
from comm import location as lo
from comm import Log
import time
import paramunittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import json
from comm import getDataFromMysql as mysql

log = Log.Log()
logger = log.get_logger()

class EboardLeave(unittest.TestCase):
    def setUp(self):
        logger.info(u"开始执行：%s"%self.__class__.__name__)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.class_name= self.__class__.__name__

    def testEboardLeave(self):
        try:
            lo.eboardLeave(self.driver,987654,987654)
            # 切换到请假界面
            lo.findByXpath(self.driver, '//div[@class="tabs--1ZJUosuiZqLp5iNz5avqjD"]/div[contains(text(), "请假")]').click()
            leave_handle = self.driver.current_window_handle
            # driver.implicitly_wait(10)
            time.sleep(1)
            # 选择请假类型
            for i in range(4):
                j = i+1
                j = json.dumps(j)
                lo.findByXpath(self.driver, '//div[@class="select--dE06ZTVGKDwzGYDBWqG_q"]').click()
                time.sleep(0.5)
                self.leave_type = lo.findByXpath(self.driver,'//div[@class="selectRoll--3I8bFXjTz6K2pGgbRyIAMm"]/span['+j+']').text
                lo.findByXpath(self.driver,'//div[@class="selectRoll--3I8bFXjTz6K2pGgbRyIAMm"]/span['+j+']').click()
                time.sleep(0.5)
                #请假开始时间
                lo.findByXpath(self.driver,'//span[@class="startTime--3IucGoWJdit6Z1oBlrKKo4 special--1JucAYb7MnXuw05NigkY7J"]').click()
                time.sleep(0.5)
                handles = self.driver.window_handles
                self.driver.switch_to_window(handles[1])
                time.sleep(0.5)
                lo.findByXpath(self.driver,'//span[@class="right--1RnycRbKAaPFSFNmtCl_BT"]').click()
                time.sleep(0.5)
                #请假结束时间
                lo.findByXpath(self.driver,'//span[@class="endTime--1jfcujQEBkSTgz9G0wLaTM special--1JucAYb7MnXuw05NigkY7J"]').click()
                time.sleep(0.5)
                handles = self.driver.window_handles
                self.driver.switch_to_window(handles[1])
                time.sleep(0.5)
                curr_time = datetime.datetime.now()
                now_day = curr_time.strftime('%Y-%m-%d %H:%M')
                end_day = (curr_time+datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
                #鼠标拖拽事件-选择请假时间
                source = lo.findByXpath(self.driver,'//div[@class="am-picker"]/div[3]/div[3]/div[1]')
                # target = lo.findByXpath(driver,'//div[@class="am-picker"]/div[3]/div[3]/div[2]')
                time_box = lo.findByXpath(self.driver,'//div[@class="am-picker"]/div[3]/div[3]').text
                time_list=str(time_box).split('\n')
                actions = ActionChains(self.driver)
                # actions.drag_and_drop(source,target)
                # actions.drag_and_drop_by_offset(source,0,-60)
                actions.click_and_hold(source)
                # actions.move_by_offset(0,-60)
                actions.drag_and_drop_by_offset(source,0,-60)
                actions.perform()

                #请假一天
                # js = 'var q=document.getElementsByClassName(\'am-picker-col-content\')[2];q.style.transform=\'translate3d(0px, -60px, 0px)\';'
                # driver.execute_script(js)
                time.sleep(0.5)
                lo.findByXpath(self.driver,'//span[@class="right--1RnycRbKAaPFSFNmtCl_BT"]').click()
                if len(time_list)>1:#非本月最后一天
                    EndTime ='function appendZero(obj) {' \
                                'if(obj<10) return "0" +""+ obj;' \
                                'else return obj;' \
                             '}' \
                         'var day = new Date();day.setTime(day.getTime());' \
                         'if(day.getMonth()<12){'\
                         'var end_time = day.getFullYear()+"-" + appendZero(day.getMonth()+1) + "-" + appendZero(day.getDate()+1)+ "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());}' \
                         'else{'\
                         'var end_time = (day.getFullYear()+1)+"-01" + "-01" + "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());}'\
                         'document.querySelector(".endTime--1jfcujQEBkSTgz9G0wLaTM").innerHTML=end_time'
                    self.driver.execute_script(EndTime)
                else:#当月最后一天
                    EndTime = 'function appendZero(obj) {' \
                              'if(obj<10) return "0" +""+ obj;' \
                              'else return obj;' \
                              '}' \
                              'var day = new Date();day.setTime(day.getTime());' \
                              'if(day.getMonth()<12){'\
                              'var end_time = day.getFullYear()+"-" + appendZero(day.getMonth()+2) + "-01" + "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());}' \
                              'if(day.getMonth()==12){' \
                              'var end_time = (day.getFullYear()+1)+"-01" + "-01" + "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());}' \
                              'document.querySelector(".endTime--1jfcujQEBkSTgz9G0wLaTM").innerHTML=end_time'
                    self.driver.execute_script(EndTime)
                time.sleep(0.5)
                #请假开始时间
                self.start_time = lo.findByXpath(self.driver,'//span[@class="startTime--3IucGoWJdit6Z1oBlrKKo4 undefined"]').text
                #请假结束时间
                end_time = lo.findByXpath(self.driver,'//span[@class="endTime--1jfcujQEBkSTgz9G0wLaTM undefined"]').text
                #请假区间
                self.StartToEnd  = self.start_time+' ~ '+end_time
                #请假原因
                reason=lo.findByXpath(self.driver,'//div[@class="am-textarea-control"]//textarea')
                reason.click()
                time.sleep(0.5)
                reason.send_keys("本人于"+str(now_day)+"请假一天,请假时间为："+self.StartToEnd+",望批准！                    ----来源于自动化测试脚本")
                self.leave_reason = str("本人于"+str(now_day)+"请假一天,请假时间为："+self.StartToEnd+",望批准！                    ----来源于自动化测试脚本")
                time.sleep(1)
                #提交
                lo.findByXpath(self.driver,'//span[@class="submit--3ko0wV8wwkVevG2AxlH6cT undefined"]').click()
                time.sleep(1)
                self.check_result(self.leave_type,self.start_time,self.leave_reason)
                continue
        except Exception as msg:
            logger.info(u"异常原因：%s"%msg)
            log.get_screen(self.driver,self.class_name)
            raise

    def check_result(self,leave_type,start_time,leave_reason):
        # 数据库查询请假记录
        sql_LeaveType ="SELECT	leave_type FROM fa_leave ORDER BY createtime desc limit 1"
        sql_LeaveReason = "SELECT reason FROM fa_leave ORDER BY createtime desc limit 1"
        db = "eboard"
        reason = mysql.getData(db, sql_LeaveReason)
        type = mysql.getData(db,sql_LeaveType)
        if self.leave_type == '病假':
            self.assertEqual(int(type[0]),0)
            logger.info(u'请假类型正确')
            leveTime = lo.findByXpath(self.driver,'//div[@class="list--2NVhVx24OJwecIMoATG2Hi"]/div[1]/span[3]').text
            self.assertIn(start_time,leveTime)
            logger.info(u'请假时间正确')
            self.assertEqual(leave_reason,str(reason[0]))
            logger.info(u'请假原因正确')

        if self.leave_type == '事假':
            self.assertEqual(int(type[0]),1)
            logger.info(u'请假类型正确')
            leveTime = lo.findByXpath(self.driver,'//div[@class="list--2NVhVx24OJwecIMoATG2Hi"]/div[1]/span[3]').text
            self.assertIn(start_time,leveTime)
            logger.info(u'请假时间正确')
            self.assertEqual(leave_reason,str(reason[0]))
            logger.info(u'请假原因正确')

        if self.leave_type == '参赛':
            self.assertEqual(int(type[0]),2)
            logger.info(u'请假类型正确')
            leveTime = lo.findByXpath(self.driver,'//div[@class="list--2NVhVx24OJwecIMoATG2Hi"]/div[1]/span[3]').text
            self.assertIn(start_time,leveTime)
            logger.info(u'请假时间正确')
            self.assertEqual(leave_reason,str(reason[0]))
            logger.info(u'请假原因正确')

        if self.leave_type == '其他':
            self.assertEqual(int(type[0]),3)
            logger.info(u'请假类型正确')
            leveTime = lo.findByXpath(self.driver,'//div[@class="list--2NVhVx24OJwecIMoATG2Hi"]/div[1]/span[3]').text
            self.assertIn(start_time,leveTime)
            logger.info(u'请假时间正确')
            self.assertEqual(leave_reason,str(reason[0]))
            logger.info(u'请假原因正确')





    def tearDown(self):
        self.driver.quit()