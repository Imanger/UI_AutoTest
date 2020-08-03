# -*- coding: utf-8 -*-
import os
import unittest
import readConfig as readConfig
from comm.Log import MyLog as Log

log = Log.get_log()
logger = log.get_logger()
filepath = ''

#设置执行用例列表
def set_case_list():
    caseList = []
    caseListPath = os.path.join(readConfig.proDir,"caseList.txt")
    fb = open(caseListPath)
    for case in fb.readlines():
        data = str(case)
        if data !="" and not data.startswith("#"):  #检查字符串是否是以指定字符串开头
            caseList.append(data.replace("\n",""))
    fb.close()
    print("---用例执行列表")
    return caseList

#设置执行用例suite
def set_suite():
    global filepath
    suite_list = unittest.TestSuite()
    suite_module = []
    case_list = set_case_list()

    for case in case_list:
        print(u"我是set_suite: "+case)

        name = str(case).split("/")[-1] #对列表字符串化并切片 文件名以”/“进行切片取最后一个
        webname = str(case).split("/")[0]
        sitename = str(case).split("/")[1]
        print("---name: "+name)
        print("---webname: "+webname)
        print("---sitename: "+sitename)
        filepath = os.path.join(readConfig.proDir,"case")#用例存放路径
        print(u"待执行用例的目录："+filepath)
        #待执行用例的目录：以递归遍历的方式找；调用用例所对应的代码
        discover = unittest.defaultTestLoader.discover(filepath,pattern=name+'.py',top_level_dir=None)
        suite_module.append(discover)#新增用例代码
    print(u"用例数量："+str(len(suite_module)))
    if len(suite_module)>0: #存在需要执行代码
        for case in suite_module:
            for name in case:
                suite_list.addTest(name)    #unittest新增进入测试集
    else:
        return None

    return suite_list

def set_website():  #读取case
    name_list = set_case_list() #赋值用例执行列表
    for case in name_list:
        data = str(case)
        if data !="" and not data.startswith("#"):
            web = data.split('/')[0]
            site = data.split('/')[1]
            name = web.upper()
            print("name: "+name)
            print("site:"+site)
            break

def get_web():
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data !="" and not data.startswith('#'):
            web = data.split("/")[0]
            break
    return web

def get_site():
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data !="" and not data.startswith('#'):
            site = data.split("/")[1]
            break
    return site

