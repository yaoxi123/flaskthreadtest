import random
import threading
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123168@127.0.0.1:3306/flasktest'
    # 设置sqlalchemy自动更新跟踪参数
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

# 创建数据库模型类
class Role(db.Model):
    """用户角色/身份表"""
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)  #模型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')   # relationship 关系

class User(db.Model):
    """用户表"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class Test(db.Model):
    __tablename__ = 'test'
    # 创建联合唯一索引
    __table_args__ = (
        UniqueConstraint(
            "nameid",
            "cardid",
            name = "name_card"
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    nameid = db.Column(db.String(64))
    cardid= db.Column(db.String(64))
    pswd = db.Column(db.String(64))

def threadtest():
    while True:
        test = Test()
        test.nameid = str(random.randint(0,9))
        test.cardid = str(random.randint(0,9))
        test.pswd = str(random.randint(0,9))
        if not Test.query.filter(Test.nameid == test.nameid,
                                 Test.cardid == test.cardid).first():
            try:
                db.session.add(test)
                db.session.commit()
                return "数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                    test.nameid, test.cardid, test.pswd)
            except Exception as e:
                return "错误:%s" % e


# @app.route('/testingthread', methods=['GET'])
def main():
    # if request.method == 'GET':
    #     while True:
    for i in range(5):
        t = threading.Thread(target=threadtest)
        t.start()
        return "正在执行多线程"

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "index-ok"
    elif request.method == "POST":
        test = Test()
        test.nameid = request.form.get("nameid")
        test.cardid = request.form.get("cardid")
        test.pswd = request.form.get("pswd")
        try:
            db.session.add(test)
            db.session.commit()
            return "数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
                test.nameid, test.cardid, test.pswd)
        except Exception as e:
            return "错误:%s" % e


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return "test-ok"
    elif request.method == "POST":
        test = Test()
        test.nameid = request.form.get("nameid")
        test.cardid = request.form.get("cardid")
        test.pswd = request.form.get("pswd")
        if Test.query.filter(Test.nameid == test.nameid,Test.cardid == test.cardid).first():
            return "数据重复nameid = %s ,cardid = %s, pswd = %s"% (
        test.nameid, test.cardid, test.pswd)
        else:
            db.session.add(test)
            db.session.commit()
            return "数据插入成功nameid = %s ,cardid = %s, pswd = %s" % (
        test.nameid, test.cardid, test.pswd)

if __name__ == '__main__':
    db.drop_all()    # 清除数据库里的所有数据
    db.create_all()  # 创建所有的表
    # test1 = Test(nameid = "1", cardid = "1", pswd = "1")
    # test2 = Test(nameid = "2", cardid = "2", pswd = "2")
    # db.session.add_all([test1,test2])
    # db.session.commit()
    app.run(debug=True)
    main()



