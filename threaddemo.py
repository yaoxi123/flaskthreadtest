#!flask/bin/python
import time
import random
import threading
from app import db
from app import Test
import multiprocessing

mutex = threading.Lock()   #创建互斥锁

def threadtest11():
    while True:
        print("11")

def threadtest22():
    while True:
        print("22")


def threadtest1():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        test.ticks = time.time()
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid,test.id != "None").first():
            try:
                db.session.add(test)
                db.session.commit()
                print("数据插入成功：nameid = %s ,cardid = %s, test.id = %s, pswd = %s" % (test.nameid, test.cardid, test.id, test.pswd))
            except Exception as e:
                print(
                    "数据插入失败：nameid = %s ,cardid = %s, test.id = %s, pswd = %s, 失败原因 = %s" % (test.nameid, test.cardid, test.id, test.pswd, e))


def threadtest2():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        test.ticks = time.time()
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid,test.id != "None").first():
            try:
                db.session.add(test)
                db.session.commit()
                print("数据插入成功：nameid = %s ,cardid = %s, test.id = %s, pswd = %s" % (test.nameid, test.cardid, test.id, test.pswd))
            except Exception as e:
                print(
                    "数据插入失败：nameid = %s ,cardid = %s, test.id = %s, pswd = %s, 失败原因 = %s" % (test.nameid, test.cardid, test.id, test.pswd, e))

def threadtest3():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        test.ticks = time.time()
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid,Test.ticks != test.ticks).first():
            try:
                db.session.add(test)
                db.session.commit()
                print("数据插入成功：nameid = %s ,cardid = %s, update_time = %s, pswd = %s" % (test.nameid, test.cardid, test.ticks, test.pswd))
            except Exception as e:
                print(
                    "数据插入失败：nameid = %s ,cardid = %s, update_time = %s, pswd = %s, 失败原因 = %s" % (test.nameid, test.cardid, test.ticks, test.pswd, e))

def main_mul():
    p1 = multiprocessing.Process(target=threadtest11)
    p2 = multiprocessing.Process(target=threadtest22)
    p1.start()
    p2.start()

def main_thrad():
    t1 = threading.Thread(target=threadtest1)
    t2 = threading.Thread(target=threadtest2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main_thrad()
