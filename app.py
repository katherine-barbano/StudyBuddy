import os
from flask import Flask, request, render_template, redirect, url_for

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

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
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect(url_for('rankings'))


@app.route('/rankings/', methods=['GET','POST'])
def rank():
    #Replace this with database info
    u1="username1"
    u2="username2"
    u3="username3"
    u4="username4"
    u5="username5"
    tag1=["code","python"]
    tag2=["python"]
    tag3=["java","python","react"]
    tag4=["code"]
    tag5=["java","python"]
    if request.method == "GET":
        return render_template("rankings.html", user1=u1,user2=u2,user3=u3,user4=u4,user5=u5,tag1=tag1,tag2=tag2,tag3=tag3,tag4=tag4,tag5=tag5)
    elif request.method == "POST":
        num=request.form['num']
        if num=="1":
            return redirect(url_for('userconnect1'))
        elif num=="2":
            return redirect(url_for('userconnect2'))
        elif num=="3":
            return redirect(url_for('userconnect3'))
        elif num=="4":
            return redirect(url_for('userconnect4'))
        elif num=="5":
            return redirect(url_for('userconnect5'))

@app.route('/userconnect1/')
@app.route('/userconnect1/<uname>')
def userconnect1():
    #pull info from database
    user="user1"#eg database[1]
    tags=["interest1","interest2"]#eg database[1]
    return render_template('userconnect.html',uname=user,tags=tags)

@app.route('/userconnect2/', methods=['GET','POST'])
@app.route('/userconnect2/<uname>')
def userconnect2():
    #pull info from database
    user="user2"#eg database[1]
    tags=["interest1","interest2"]#eg database[1]
    return render_template('userconnect.html',uname=user,tags=tags)

@app.route('/userconnect3/', methods=['GET','POST'])
@app.route('/userconnect3/<uname>')
def userconnect3():
    #pull info from database
    user="user3"#eg database[2]
    tags=["interest1","interest2"]#eg database[1]
    return render_template('userconnect.html',uname=user,tags=tags)

@app.route('/userconnect4/', methods=['GET','POST'])
@app.route('/userconnect4/<uname>')
def userconnect4():
    #pull info from database
    user="user4"#eg database[3]
    tags=["interest1","interest2"]#eg database[1]
    return render_template('userconnect.html',uname=user,tags=tags)

@app.route('/userconnect5/', methods=['GET','POST'])
@app.route('/userconnect5/<uname>')
def userconnect5():
    #pull info from database
    user="user5"#eg database[4]
    tags=["interest1","interest2"]#eg database[1]
    return render_template('userconnect.html',uname=user,tags=tags)

    

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        final_dict = {}
        tags_processed = []
        tags=request.form['tags'].split(',')
        for item in tags:
            tags_processed.append(item.strip().lower())
        final_dict['tags'] = tags_processed
        return redirect(url_for('index'))