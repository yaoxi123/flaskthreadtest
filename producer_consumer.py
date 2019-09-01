import threading
import queue
import time
import random
from app import db
from app import Test


condition = threading.Condition()


# 生产者
def producer(i, q):
    print(f'生产者子线程{i}开始执行')

    while True:
        with condition:
            value = random.randint(0,100)
            if not q.full():
                print(f'生产者子线程{i},生产了{value}')
                test = Test()
                test.nameid = str(random.randint(0, 9))
                test.cardid = str(random.randint(0, 9))
                test.pswd = str(random.randint(0, 9))
                test.ticks = time.time()
                if not Test.query.filter(Test.nameid == test.nameid,
                                         Test.cardid == test.cardid).first():
                    try:
                        db.session.add(test)
                        db.session.commit()
                        print(
                            "数据插入成功：nameid = %s ,cardid = %s, pswd = %s" % (
                            test.nameid, test.cardid, test.pswd))
                    except Exception as e:
                        print(
                            "数据插入失败：nameid = %s ,cardid = %s, pswd = %s, 失败原因 = %s" % (
                            test.nameid, test.cardid, test.pswd, e))
                q.put(value)
            else:
                # 通知消费者消费
                print('队列已满,请消费')
                condition.wait()
                condition.notify_all()


# 消费者
def consumer(i, q):
    print(f'消费者子线程{i}开始执行')
    while True:
        with condition:
            if not q.empty():
                value = q.get()
                print(f'消费者子线程{i}, 消费了{value}')
                time.sleep(1)
            else:
                # 通知生产者生产
                print('队列已空,请生产.')
                condition.notify_all()
                condition.wait()


if __name__ == '__main__':
    print('主线程开始')
    q = queue.Queue(10)

    # 生产者线程
    for i in range(5):
        threading.Thread(target=producer, args=(i,q)).start()

    # 消费者线程
    for i in range(4):
        threading.Thread(target=consumer, args=(i, q)).start()

    print('主线程结束')
