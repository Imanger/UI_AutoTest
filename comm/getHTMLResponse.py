#获取页面数据，解析响应结果
import urllib.request
from urllib import parse
from urllib import  request
import json
import ssl
from comm import sendEmail
from urllib import parse

#ssl取消全局验证
ssl._create_default_https_context = ssl._create_unverified_context

def requestHtml(params,cookie):
    headers = {
        'Cookie': cookie
    }
    url = 'https://lesson.leke.cn/auth/provost/paike/rule/getTeachPlans.htm'
    qs = parse.urlencode(params)
    url = url + "?" + qs
    req = urllib.request.Request(url,headers=headers)
    # response = urllib.request.urlopen(req)

    with request.urlopen(req) as f:
        for m, i in f.getheaders():
            print('%s: %s' % (m,i))
        data = f.read().decode('utf-8')
        dict_data = json.loads(data)
        plan = dict_data['subPlans']
        list_res=list_dictionary(plan)
        return list_res



def list_dictionary(d):
    list_data = []

    for k, v in d.items():
        if isinstance(v, dict):
            list_dictionary(v)
        else:
            list_data.append(v)
    return list_data



# url='https://lesson.leke.cn/auth/provost/paike/rule/getTeachPlans.htm?paikeTaskId=2936&weekType=1&spm=104057'
# requestHtml(url,1)