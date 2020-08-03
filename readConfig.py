import os
import codecs
import configparser


proDir = os.path.split(os.path.realpath(__file__))[0]#获取当前执行脚本的绝对路径；如果给出的是一个目录和文件名，则输入路径和文件名
configPath = os.path.join(proDir,'config.ini').replace("\\","/")#y以上目录，组合成新目录

class ReadConfig:
    def __init__(self):
        ft = open(configPath)#打开config.ini
        data = ft.read()#读取数据

        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            f = codecs.open(configPath,'w',encoding='utf-8')    #读取文件：|w|仅写，若文件已存在，内容将先被清空
            f.write(data)
            f.close()
        ft.close()

        self.cf = configparser.ConfigParser()#读取配置包，初始化实例
        self.cf.read(configPath)

    def get_webServer(self,section,param):  #获取ini文件中的section和param
        '''
        get value by name
        :param name1:
        :param name2:
        :return:
        '''
        value = self.cf.get(section,param)
        print(value)
        return value