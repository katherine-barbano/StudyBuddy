import os
from flask import Flask, request, render_template, redirect, url_for

from dotenv import load_dotenv
load_dotenv()

global number#fix global
number=0

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
        sentence=request.form['goal']
        return redirect(url_for('rankings'))


@app.route('/rankings/', methods=['GET','POST'])
def rank():
    #Retrieve info from database. Assumes info in form of 3 arrays
    #userArray=['user1','user2','user3','user4','user5']
    #goalArray=['goal1','goal2','goal3','goal4','goal5']
    #tagArray=[['flask','node'],['code'],['flask'],['fun','microsoft','java'],['swift']]#nested array
    if request.method == "GET":#somehow need to get these arrays + database info into rankings.html table info
        return render_template("rankings.html")
    elif request.method == "POST":
        #number=request.form['rankings']
        return redirect(url_for('userconnect'))

@app.route('/userconnect/', methods=['GET','POST'])
def selectedUserInfo():
    #if request.method=='GET':
    #    return render_template("userconnect.html")
    return number#need to display the correct user
    

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