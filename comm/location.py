# -*- coding: utf-8 -*-
#公共方法的封装

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.select import Select


def findById(driver, id):
    f = driver.find_element_by_id(id)
    return f


def findByName(driver, name):
    f = driver.find_element_by_name(name)
    return f


def findByClass(driver, name):
    f = driver.find_element_by_class_name(name)
    return f


def findByTagName(driver, name):
    f = driver.find_element_by_tag_name(name)
    return f


def findByLinkText(driver, link_text):
    f = driver.find_element_by_link_text(link_text)
    return f


def findByPartialLinkText(driver, link_text):
    f = driver.find_element_by_partial_link_text(link_text)
    return f


def findByXpath(driver, xpath):
    f = driver.find_element_by_xpath(xpath)
    return f


def findByCssSelector(driver, css_selector):
    f = driver.find_element_by_css_selector(css_selector)
    return f

#乐课登录
def login(driver,loginName,password):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get('https://cas.leke.cn/login')
    findByXpath(driver,'//*[@id="loginName"]').send_keys(loginName)
    time.sleep(0.5)
    findByXpath(driver,'//*[@id="password"]').send_keys(password)
    time.sleep(0.5)
    element=findById(driver,'j-sign-on')
    element.click()
#班牌登录
def eboardLogin(driver,loginName,password):
    driver.get('https://webapp.leke.cn/electrClassbrand/index.html#/')
    for i in range(10):  # 允许弹框出现的次数，一直循环的直接放弃
        time.sleep(0.5)
        try:
            links = findByXpath(driver, '//input[@type="text"]')
            break
        except Exception as e:
            if 'alert' in str(e):
                alert1 = driver.switch_to.alert
                alert1.dismiss()
            else:
                links = []
                break
    #获取当前句柄
    login_handle = driver.current_window_handle
    findByXpath(driver, '//input[@type="text"]').send_keys(loginName)
    time.sleep(1)
    findByXpath(driver, '//input[@type="password"]').send_keys(password)
    time.sleep(1)
    findByXpath(driver, '//input[@type="button"]').click()

#班牌查看考试报告
def eboardReport(driver,loginName,password):
    driver.get('https://webapp.leke.cn/electrClassbrand/index.html#/')
    for i in range(10):  # 允许弹框出现的次数，一直循环的直接放弃
        time.sleep(1)
        try:
            links = findByXpath(driver, '//input[@type="text"]')
            break
        except Exception as e:
            if 'alert' in str(e):
                alert1 = driver.switch_to.alert
                alert1.dismiss()
            else:
                links = []
                break
    # 获取当前句柄
    login_handle = driver.current_window_handle
    findByXpath(driver, '//input[@type="text"]').send_keys(loginName)
    time.sleep(1)
    findByXpath(driver, '//input[@type="password"]').send_keys(password)
    time.sleep(1)
    findByXpath(driver, '//input[@type="button"]').click()
    time.sleep(2)
    js = 'window.open("https://webapp.leke.cn/electrClassbrand/index.html#/personalCenter/detail?user_name=ddd&user_id=1221497")'
    driver.execute_script(js)
    time.sleep(1)
    handles = driver.window_handles
    # person_handle = None
    # for handle in handles:
    #     if handle == login_handle:
    #         person_handle = handle

    #解决新页面再次弹框问题
    driver.switch_to.window(handles[0])
    time.sleep(1)
    driver.switch_to.window(handles[1])
    driver.implicitly_wait(10)
    time.sleep(1)
    #查看报告
    findByXpath(driver,"//div[@class='tableList--2O41IqzmNeKSSsQQ11F-ja']/div[6]/div[5]/a").click()


#班牌个人中心请假
def eboardLeave(driver,loginName,password):
    driver.get('https://webapp.leke.cn/electrClassbrand/index.html#/')
    for i in range(10):  # 允许弹框出现的次数，一直循环的直接放弃
        time.sleep(0.5)
        try:
            links = findByXpath(driver, '//input[@type="text"]')
            break
        except Exception as e:
            if 'alert' in str(e):
                alert1 = driver.switch_to.alert
                alert1.dismiss()
            else:
                links = []
                break
    # 获取当前句柄
    login_handle = driver.current_window_handle
    findByXpath(driver, '//input[@type="text"]').send_keys(loginName)
    time.sleep(1)
    findByXpath(driver, '//input[@type="password"]').send_keys(password)
    time.sleep(1)
    findByXpath(driver, '//input[@type="button"]').click()
    time.sleep(2)
    js = 'window.open("https://webapp.leke.cn/electrClassbrand/index.html#/personalCenter/detail?user_name=ddd&user_id=1221497")'
    driver.execute_script(js)
    time.sleep(0.5)
    handles = driver.window_handles

    # 解决新页面再次弹框问题
    driver.switch_to.window(handles[0])
    time.sleep(1)
    driver.switch_to.window(handles[1])
    driver.implicitly_wait(10)


