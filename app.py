import os
from flask import Flask, request, render_template, redirect,url_for
# from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import create_engine, MetaData
import pyodbc

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# client = MongoClient("mongodb://127.0.0.1:20101/") #host uri
# db = client['admin']    #Select the database
# db.authenticate(name="localhost",password='C2y6yDjf5' + r'/R' + '+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw' + r'/Jw==')

## Comment out when running locally
# client = MongoClient(os.getenv("MONGOURL"))
# db = client['admin']    #Select the database
# # print(db)
# # db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))
# todos = db.todo #Select the collection
# print(todos)
password = os.getenv("DB_PASSWORD")

# Configure Database URI:
print(os.getenv("DB_PASSWORD"))
params = urllib.parse.quote_plus \
(r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:studybuddy.database.windows.net,1433;Database=studybuddy;Uid=studybuddy;Pwd=Buddystudy1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')


# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
conf_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

engine_azure = create_engine(conf_str, echo=True)
print('connection is ok')
print(engine_azure.table_names())

db = SQLAlchemy(app)

#Relation database
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     uname = db.Column(db.String(80), unique=True, nullable=False)
#     pswd = db.Column(db.String(80), nullable=False)
#     tg = db.relationship("Tag", secondary=lambda: usertags_table)
#
#     def __init__(self, uname, pswd):
#         self.uname = uname
#         self.pswd = pswd
#     #     # self.tags = tag
#     def __repr__(self):
#         return '<User %r>' % self.uname
#
#     tags = association_proxy('tg', 'tag')
#
# class Tag(db.Model):
#     __tablename__ = 'tag'
#     id = db.Column(db.Integer, primary_key=True)
#     tag = db.Column(db.String(80), unique=True, primary_key=True)
#
#     def __init__(self, tag):
#         self.tag = tag
#
#     def __repr__(self):
#         return '<Tag %r>' % self.tag
#
#
# meta = MetaData()
# usertags_table=db.Table('usertags', meta,
#     db.Column('user_id', db.Integer, db.ForeignKey("user.id"),
#            primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey("tag.id"),
#            primary_key=True))


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages'))
     def __init__(self, uname, pswd):
            self.uname = uname
            self.pswd = pswd


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), unique=True, primary_key=True)

        def __init__(self, tag):
            self.tag = tag


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # User is requesting the form
        return render_template('login.html')
    elif request.method == 'POST':
        # User has sent us data
        return redirect(url_for('index'))

@app.route('/index')
def index():
    return "Good you have logged in"

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    db.create_all()
    # meta.create_all()
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        print("hello")
        print(request.form['uname'])

        final_dict = {}
        tags_processed = []
        for item in request.form['tags'].split():
            format_tag = item.strip(',').lower()
            new_tag = Tag(format_tag)
            db.session.add(new_tag)
            print(format_tag)
            # db.session.commit()
            # new_tag = Tag(format_tag)
            print(new_user.tags)
            # new_user.tags.append(format_tag)
        new_user = User(uname=request.form['uname'], pswd=request.form['psw'])
        db.session.add(new_user)
        db.session.commit()
        new_user.Query.all()
            # tags_processed.append(item.strip().lower())
        # final_dict['tags'] = tags_processed

        return redirect(url_for('index'))
