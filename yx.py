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

        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            try:
                # mutex.acquire()  # 上锁
                db.session.add(test)
                # mutex.release()  # 解锁
                db.session.commit()
                print("数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (
                test.nameid, test.cardid, test.pswd, e))


def threadtest2():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        # mutex.acquire()  # 上锁
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            try:

                # mutex.acquire()  # 上锁
                db.session.add(test)
                # mutex.release()  # 解锁
                db.session.commit()
                print("数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
        # mutex.release()  # 解锁
                # break

def threadtest3():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        test.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid,Test.update_time != test.update_time).first():
            try:
                db.session.add(test)
                db.session.commit()
                print("数据插入成功：nameid = %s ,cardid = %s, update_time = %d, pswd = %s" % (test.nameid, test.cardid, test.update_time, test.pswd))
            except Exception as e:
                print(
                    "数据插入成功：nameid = %s ,cardid = %s, update_time = %d, pswd = %s" % (test.nameid, test.cardid, test.update_time, test.pswd, e))
                # break

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
