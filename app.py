from flask import Flask, render_template, flash, request,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import config



app = Flask(__name__)

# 数据库配置: 数据库地址/关闭自动跟踪修改
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=Driver%3D%7BODBC+Driver+17+for+SQL+Server%7D%3BServer%3Dtcp%3Atest1-server.database.windows.net%3BDatabase%3Dtest1database%3BUid%3Dlancer%3BPwd%3DLrd19970323%3BEncrypt%3Dyes%3BTrustServerCertificate%3Dno%3BConnection+Timeout%3D30%3B'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://lancer:Lrd19970323@test1-server.database.windows.net/test1database?driver=ODBC+Driver+17+for+SQL+Server&charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'itheima'

db = SQLAlchemy(app)
print('db initialized...')

class Author(db.Model):
    # 表名
    __tablename__ = 'authors'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 关系引用
    # books是给自己(Author模型)用的, author是给Book模型用的
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author: %s' % self.name

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s %s' % (self.name, self.author_id)


@app.route('/')
def hello_world():
    return 'Hello World!'



db.drop_all()
db.create_all()
print('db creating...')
# 生成数据
au1 = Author(name='lancer')
au2 = Author(name='fuck')
au3 = Author(name='you')
# 把数据提交给用户会话
db.session.add_all([au1, au2, au3])
# 提交会话
db.session.commit()
bk1 = Book(name='老王回忆录', author_id=au1.id)
bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
# 把数据提交给用户会话
db.session.add_all([bk1, bk2, bk3, bk4, bk5])
# 提交会话
db.session.commit()

app.run(debug=True)