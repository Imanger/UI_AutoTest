# -*- coding: utf-8 -*-
from pymongo import MongoClient

def getData(db,collections,query,projection):

    DATABASE_IP = '192.168.20.74'
    DATABASE_PORT = 27018

    client = MongoClient(DATABASE_IP,DATABASE_PORT)
    db_auth = client.admin
    db_auth.authenticate('alpha','sqrj@alpha#16888')
    db = client[db]
    col = db[collections]

    if projection =={}:
        for x in col.find(query):
            print(x)
            return (x)
    if projection !={}:
        for x in col.find(query,projection):
            print(x)
            return (x)




