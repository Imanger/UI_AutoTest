# -*- coding: utf-8 -*-
import os
import logging
import threading
import time
import readConfig
from selenium import webdriver

localReadConfig = readConfig.ReadConfig()
date_time = str(time.strftime('%Y%m%d%H%M%S',time.localtime()))

class Log:
    def __init__(self):

        global result,logPath,logFilePath

        result = os.path.join(readConfig.proDir,'result')#日志结果存放的地址

        if not os.path.exists(result):  #如果目录不存在，则新建该目录
            os.mkdir(result)

        logFilePath = os.path.join(result,date_time)    #拼接日志文件名称与路径
        if not os.path.exists(logFilePath):
            os.mkdir(logFilePath)   #如果不存在目录，则新建该目录

        #日志文件全路径
        logPath = os.path.join(logFilePath,'result.log')
        print('logPath: '+logPath)

        '''
        创建logger
        创建handler
        定义formatter
        给handler添加formatter
        给logger添加handler
        '''
        #创建一个logger
        self.logger = logging.getLogger()

        if not self.logger.handlers:
            #定义输入日志级别
            self.logger.setLevel(logging.INFO)
            #创建一个handler，用于写入日志,处理器
            self.handler = logging.FileHandler(filename=logPath,encoding='utf-8')
            #定义handler的输出格式
            self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            #handler添加formatter
            self.handler.setFormatter(self.formatter)
            #为日志器logger添加上面创建的处理器handler
            self.logger.addHandler(self.handler)

    def get_logger(self):
        return self.logger

    def build_start_line(self,name):
        line = '**********'+name+'START************'
        self.logger.info(line)

    def build_end_line(self,name):
        line = '**********' + name + 'END************'
        self.logger.info(line)

    def get_logfile_path(self):
        return logFilePath

    def get_log_path(self):
        return logPath

    def get_report_path(self):
        report_path = os.path.join(logFilePath,'report.html')
        return report_path

    def get_screen(self,driver,class_name):
        now = time.strftime('%Y%m%d_%H%M%S')
        pic_name = str('%s'%class_name+'_'+'%s'%now+'.png')
        pic_url = os.path.join(logFilePath,pic_name)
        print(pic_url)
        driver.get_screenshot_as_file(pic_url)


class MyLog:
    log = None
    mutex = threading.Lock()#创建锁

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()#锁定
            MyLog.log = Log()
            MyLog.mutex.release()#释放锁
        return MyLog.log


if __name__=='__main__':
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.info('test info')