# -*- coding: utf-8 -*-
# @Time : 2020-04-10
# @Autor : zhiying.liu

import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import random

def oa_update():
    url = 'http://oa.16888.hk/API/Attendance/updateClock.htm'
    data = {"latlon":"dk9g+3BNi6mTUJfZ2cJUkNR4yJfkAcmcyPDhYuJjMSBi80ow+UvHv1Myjw6i7j8doRy5VuuaaXUBKuFxn8razNWhzwHKZLBaue5PYK8lolauYUrzZinMmfaEwKNjoP5W6NSMFdKdOK+RFrXw2CeROtR4YyvWZ0WeOcydvhwE+v+vL8urgcxf1qE6sinb1ToKS4uMcbCNg2g81w144jLHiQ==",
            "clockId":"1692316",
            "userInfo":"1iHTO/vVCKnI0cSvwI4iNBSeNmvlpAOkNj9BaiAvB9fHbLKqsmvjpHlQYytQOM+gS24KUz5YSWt/jzXR/DnwLe8m5UAdPQYEQz1129V89PI9fp4cOCg7aDt4IEoLnigRRq+8A0a0fhwamOAl8NTIvcrEHUOKDybAqSr1BKiYgww=",
            "phoneID":"ABQ88B7P/RD7TZvCn1a+XELweeZpELskEyhyhZxQffNZEVYuGwcFqmgW+haqRicX"}

    response = requests.post(url,data=data)
    SERVERCHAN_KEY = 'SCU68701T774d474faf2054af7599f814b9515af25df3590ff0fa2'
    api = 'https://sc.ftqq.com/' + SERVERCHAN_KEY + '.send'
    title = "打卡结果通知"
    content = response.text

    data = {
        "text":title+datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "desp":content
    }
    req = requests.post(api,data=data)
    print(req)
    print(response.text)
    print("消息推送成功!")

def oa_punchClock():
    # second = randomSeconds()
    url = 'http://oa.16888.hk/API/Attendance/punchClock.htm'
    data = {"latlon":"dk9g+3BNi6mTUJfZ2cJUkNR4yJfkAcmcyPDhYuJjMSBi80ow+UvHv1Myjw6i7j8doRy5VuuaaXUBKuFxn8razNWhzwHKZLBaue5PYK8lolauYUrzZinMmfaEwKNjoP5W6NSMFdKdOK+RFrXw2CeROtR4YyvWZ0WeOcydvhwE+v+vL8urgcxf1qE6sinb1ToKS4uMcbCNg2g81w144jLHiQ==",
            "clockId":"1672542",
            "userInfo":"1iHTO/vVCKnI0cSvwI4iNBSeNmvlpAOkNj9BaiAvB9fHbLKqsmvjpHlQYytQOM+gS24KUz5YSWt/jzXR/DnwLe8m5UAdPQYEQz1129V89PI9fp4cOCg7aDt4IEoLnigRRq+8A0a0fhwamOAl8NTIvcrEHUOKDybAqSr1BKiYgww=",
            "phoneID":"ABQ88B7P/RD7TZvCn1a+XELweeZpELskEyhyhZxQffNZEVYuGwcFqmgW+haqRicX"}

    response = requests.post(url,data=data)
    SERVERCHAN_KEY = 'SCU68701T774d474faf2054af7599f814b9515af25df3590ff0fa2'
    api = 'https://sc.ftqq.com/' + SERVERCHAN_KEY + '.send'
    title = "打卡结果通知"
    content = response.text

    data = {
        "text":title+datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "desp":content
    }
    req = requests.post(api,data=data)
    print(req)
    print(response.text)
    print("消息推送成功!")

def randomSeconds():
    return random.randint(0,60)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    try:
        scheduler.add_job(oa_punchClock, 'cron', day_of_week='mon-fri', hour=8, minute=random.randint(35, 50),
                          second=random.randint(0, 60),misfire_grace_time=10)
        scheduler.add_job(oa_punchClock, 'cron', day_of_week='mon-fri',hour=21, minute=random.randint(4, 7),
                                  second=random.randint(0,60),misfire_grace_time=10)
        # scheduler.add_job(oa_punchClock, 'cron', hour=8, minute=random.randint(0, 5),
        #                   second=random.randint(0, 60),misfire_grace_time=10)
        # scheduler.add_job(oa_punchClock, 'cron', hour=21, minute=random.randint(0, 10),
        #                   second=random.randint(0, 60), misfire_grace_time=10)
    except Exception as e:
        oa_punchClock()

    # scheduler.add_job(oa_update, 'cron', hour=21, minute=random.randint(0, 10), second=random.randint(0, 60))
    # oa_punchClock()
    print('定时任务启动成功！')

    try:
        scheduler.start()
    except(KeyboardInterrupt,SystemExit):
        print("定时任务挂了！")


