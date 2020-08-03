# -*- coding: utf-8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder


host = "192.168.20.75"
port = 61306
user = "lekeEduAdmin"
passwd = "Q2wtjmuz"
charset = "utf8"


def getData(db,sql):
    #打开数据库链接
    dbconn = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=passwd,
                             db=db,
                             charset=charset)
    #使用cursor()方法获取操作游标(用于发送和接收数据)
    cursor = dbconn.cursor()
    #执行sql语句
    cursor.execute(sql)
    #fetchone获取一条数据
    data = cursor.fetchone()
    #关闭游标
    cursor.close()
    #关闭数据库连接，释放数据库资源
    dbconn.close()
    #返回数据
    print(str(data))
    return data

#更新数据
def UpdateDate(db,sql):
    # 打开数据库链接
    dbconn = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=passwd,
                             db=db,
                             charset=charset)
    cursor = dbconn.cursor()
    count = cursor.execute(sql)
    dbconn.commit()
    cursor.close()
    dbconn.close()
    return count

#插入数据，并返回数据主键
def insertData(db,sql):
    dbconn = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=passwd,
                             db=db,
                             charset=charset)
    cursor = dbconn.cursor()
    cursor.execute(sql)
    last_id = dbconn.insert_id()
    dbconn.commit()
    cursor.close()
    dbconn.close()
    return last_id

#删除数据
def deleteData(db,sql):
    dbconn = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=passwd,
                             db=db,
                             charset=charset)
    cursor = dbconn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    dbconn.commit()
    cursor.close()
    dbconn.close()
    return data




