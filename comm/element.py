# -*- coding: utf-8 -*-
#公共方法封装

from selenium.common.exceptions import  NoSuchElementException

def isElementExist(self,element):
    flag = True
    driver = self.driver
    try:
        driver.find_element_by_xpath(element)
    except NoSuchElementException:
        flag = False
        return flag
