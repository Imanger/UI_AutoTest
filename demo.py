# # # -*- coding: utf-8 -*-
# import requests
# Object={'obj_1':'1','obj_2':'2'}
# t=Object.get('boj_1','3')
# print(t)
#
# print(0.1+0.2)
#
# object=(1, 2, 3, 4, 5)
# object2 = [1,2,3,4,5]
# print(object[:3])
# print(object[1:3])
# print(object2[:3])
# #(1,2,3)
#
# object="12345"
# print(object[::-1])
# #54321
#
# state_dict = {'start': 1, 'running': 2, 'offline': 3, 'unknown': 4}
# code = state_dict.get('asd', 5)
# print(code)
#
#
#
# def default_para_trap(para=[],value=0):
#     print(id(para))
#     if not para:
#         para = []
#         print(id(para))
#     para.append(value)
#     return para
#
#
# print('第一步:{}'.format(default_para_trap(value=100)))
#
# print('第二步:{}'.format(default_para_trap(value=50)))
#
# info={'name':'张三', 'age':19, 'score':{'python':95,'math':92}}
# print(info['name'])
# print(info['score']['python'])
#
# # n=eval(input('请输入一个大于0的整数：'))
# # sum = 0
# # for i in range(1,n+1,2):
# #     sum+=i
# # print(sum)
#
# m,n=24,36
# while m!=n:
#     while m>n:
#         m-=n
#     while n>m:
#         n-=m
# print(m)
#
# def ModifyVal(x,y):
#     x=y
# def ModifyListElement(ls,idx,val):
#     ls[idx]=val
# c=[1,3,5]
# ModifyVal(c,[4,5,6])
# print(c)
# c=[2,4,6,8]
# ModifyListElement(c,2,20)
# print(c)
#
#
# def Sum(a,b,c):
#     print(a+b+c)
# t=(1,2,3)
# Sum(*t)
#
# sum=0
# for i in range(1,11):
#     sum+=i
# print('求和结果：%d'%sum)
#
# def f1():
#     print('f1函数被调用！')
# def f2():
#     print('f2函数被调用！')
# f1=f2
# f1()
# f2()
#
#
# def FunAdd(f,x,y):
#     return f(x)+f(y)
# print(FunAdd(lambda x:x*2+1,3,-5))#-2
# print(FunAdd(lambda x:x**2+1,3,-5))#36
#
#
# def outer(x):
#     def inner(y):
#         nonlocal x
#         return x+y
#     return inner
# f=outer(5)
# print(f(20))
#
#
#
# class Student:
#     pass
# if __name__=='__main__':
#     stu1=Student()
#     stu2=Student()
#     Student.name='unknown'
#     stu1.age=19
#     print(stu1.name) #输出unknown
#     print(stu2.name) #输出unknown
#     print(stu1.age) #输出19
#     print(stu2.age) #取消前面的注释符则会报错
#
#
# def all_unique(lst):
#     return len(lst) == len(set(lst))
#
# x = [1,1,2,2,3,2,4,4,3,5,6]
# y = [1,2,3,4,5,6]
# m=set(x)
# print(m)
# print(all_unique(x)) #false
# print(all_unique(y)) #true


# adict = {'name': 'kyda', 'age': 10}
# seq=(1,2,3)
# adict.fromkeys(seq,value=None)

#
# class A(object):
#     # 属性默认为类属性（可以给直接被类本身调用）
#     num = "类属性"
#
#     # 实例化方法（必须实例化类之后才能被调用）
#     def func1(self):  # self : 表示实例化类后的地址id
#         print("func1")
#         print(self)
#
#     # 类方法（不需要实例化类就可以被类本身调用）
#     @classmethod
#     def func2(cls):  # cls : 表示没用被实例化的类本身
#         print("func2")
#         print(cls)
#         print(cls.num)
#         cls().func1()
#
#     # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
#     def func3():
#         print("func3")
#         print(A.num)  # 属性是可以直接用类本身调用的
#
#
# # A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
# A.func2()
# # A.func3()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# print (u'当前URL为:',driver.current_url)
#
# driver.find_element_by_link_text(u'新闻').click()
# print (u'当前Url为:',driver.current_url)#获取当前路径
#
# print (u'当前Url为:',driver.page_source)#page_souce获取当前网页源代码
# driver.quit()


#获取页面数据，解析响应结果
import urllib.request
from urllib import parse
from urllib import  request
import json
import ssl

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
    print("列表：",dict_data.items())

# def list_dictionary(data):
#     for key,val in data.items():
#         try:
#             print('\nkey:'+key)
#             list_dictionary(val)
#         except AttributeError as e:
#             print("value:"+str(val)+'\n')

def myprint(d):
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v)
    else:
      print("{0} : {1}".format(k, v))

myprint(dict_data)
    # print('Data:',dict_data)

    # data = f.read().decode('utf-8')
    # retdata = eval(data)
    # print(retdata)


# html = response.read().decode('utf-8')
# print(html)



# print(html)


# # parse_qs函数的用法
# from urllib import parse
# from urllib import request
# url = 'http://www.baidu.com/s'
# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# print(qs)
# url = url + "?" + qs
# resp = request.urlopen(url)
# print(resp.read())


famous_person = "Steve Jobs once said"
message = "You've got to find what you love"
yiqi = famous_person + ',''"'+message+'"'
print(yiqi)


from urllib import parse
import time
url='https://webapp.leke.cn/lesson-web/index.html#/smartPaike/lessonPlan/courseTeachers?paikeTaskId=2937&weekType=1&spm=104057'
# result = parse.urlparse( url )
# print(result)

print('1111'+parse.urlparse(url).path)
urldata = "http://en.wikipedia.org/w/api.php?action=query&ctitle=FA"
result = parse.urlparse(url).fragment
print (result)

params=(url.split('?')[1]).split('&')
print(params)
for i in params:
    t=i.split('=')
    print(dict(zip(t[0::2],t[1::2])))

# b = dict(zip(params[0::2],params[1::2]))#从0开始步长为2
b= dict([s.split('=')for s in params])
print(b)