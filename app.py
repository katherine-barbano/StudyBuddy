import os
from flask import Flask, request, render_template, redirect, url_for
from context import example_input, apply
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

def user_find(uname):
    for person in example_input['people']:
        if uname == person['name']:
            return person
    return False


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # User is requesting the form
        return render_template('login.html')
    elif request.method == 'POST':
        # User has sent us data
        try:
            name = request.form['uname']
            if not user_find(name):
                return render_template('login.html', error=True)
            return redirect('/u/{}'.format(name))
        except:
            return render_template('login.html', error=True)

@app.route('/u/<uname>/', methods=['GET', 'POST'])
def index(uname):
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect('/u/{}/rankings/'.format(uname))


@app.route('/u/<uname>/rankings/', methods=['GET','POST'])
def rank(uname):
    #Replace this with database info
    if request.method == "GET":
        try: 
            api_call = apply(example_input, uname)
            ranked_list = api_call['results']
        except:
            return "Sorry, your account does not exist"
        print(ranked_list)
        ranked_list = ranked_list[:5]
        final_context = []
        for i, item in enumerate(ranked_list):
            item_name = item[0]
            user = user_find(item_name)
            final_context.append({"num": i+1, "name": item_name, "tags": user['interests'][:5]})
        return render_template("rankings.html", data=final_context)
    elif request.method == "POST":
        name = request.form['name']
        return redirect('/userconnect/{}/.'.format(name))

@app.route('/userconnect/<uname>/')
def userconnect(uname=''):
    #pull info from database
    user = user_find(uname)
    tags = user['interests']
    return render_template('userconnect.html',uname=uname,tags=tags)

    

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
        example_input['people'].append({'name': request.form['uname'], 'interests': tags_processed})
        return redirect('/u/{}/'.format(request.form['uname']))