#!flask/bin/python
# FAIL
import random
import threading
from app import db
from app import Test
import multiprocessing

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
        if Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            Test.nameid = test.nameid
            Test.cardid = test.cardid
            test.pswd = str(random.randint(0, 9))
            try:
                db.session.add(test)
                db.session.commit()
                print("TRUE--数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("TRUE--数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
        else:
            try:
                db.session.add(test)
                db.session.commit()
                print("FALSE--数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("FALSE--数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
                # break

def threadtest2():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        if Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            Test.nameid = test.nameid
            Test.cardid = test.cardid
            test.pswd = str(random.randint(0, 9))
            try:
                db.session.add(test)
                db.session.commit()
                print("TRUE--数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("TRUE--数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
        else:
            try:
                db.session.add(test)
                db.session.commit()
                print("FALSE--数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("FALSE--数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
                # break

def threadtest3():
    while True:
        test = Test()
        test.nameid = str(random.randint(0, 9))
        test.cardid = str(random.randint(0, 9))
        test.pswd = str(random.randint(0, 9))
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            try:
                db.session.add(test)
                db.session.commit()
                print("数据插入失败nameid = %s ,cardid = %s, pswd = %s" % (test.nameid, test.cardid, test.pswd))
            except Exception as e:
                print("数据插入失败nameid = %s ,cardid = %s, pswd = %s，错误原因 = %s" % (test.nameid, test.cardid, test.pswd, e))
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
