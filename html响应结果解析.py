#获取页面数据，解析响应结果
import urllib.request
from urllib import parse
from urllib import  request
import json
import ssl
from comm import sendEmail

#ssl取消全局验证
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
           'Cookie' : r'UM_distinctid=16ecacc4603773-0caf508413f509-2393f61-1fa400-16ecacc46047d2; Hm_lvt_1cc429d7f39859f7f65470f59284e944=1574853581,1574916855,1575339602,1575360415; ticket="VFdwclBRPT07TFMwcUxDMGtMU1VxOzI5Mjk="; _nk_=%E6%95%99%E5%8A%A11; JSESSIONID=A8CC5E5C7E3FE5C6F39DC843B177DB6F; CNZZDATA1277206897=450406635-1574848387-https%253A%252F%252Fcas.leke.cn%252F%7C1575362084; _hb=1; Hm_lpvt_1cc429d7f39859f7f65470f59284e944=1575362765'
           }
params = {"paikeTaskId":2936,
          "weekType":1}
qs = parse.urlencode(params)
print(qs)
url = 'https://lesson.leke.cn/auth/provost/paike/rule/getTeachPlans.htm'
url = url + "?" + qs
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
print(response)
print(req)

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    print(f.getheader('Server'))
    for m, i in f.getheaders():
        print('%s: %s' % (m,i))
    data = f.read().decode('utf-8')
    print(type(data))
    print(data)
    dict_data = json.loads(data)
    print(type(dict_data))

    print("列表：",dict_data['subPlans'])
    plan=dict_data['subPlans']



list_dic = []
def list_dictionary(d):
    for k, v in d.items():

        if isinstance(v, dict):
            list_dictionary(v)
        else:
            # val=("{0} : {1}".format(k, v))
            # val = v
            # print('type=',type(val))

            list_dic.append(v)
    return (list_dic)


list_dictionary(plan)

list_params=[]
for i in list_dic:
    for j in i:
        for key,val in j.items():
            list_params.append("{0}:{1}".format(key,val))

print(list_params)

for m in list_dic:
    for n in m:
        print('元素：',n.get('subName'),n.get('weekCnt'))