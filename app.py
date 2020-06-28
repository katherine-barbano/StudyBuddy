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
    return "Good you have logged in"

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        final_dict = {}
        tags_processed = []
        for item in request.form['tags']:
            tags_processed.append(item.strip().lower())
        final_dict['tags'] = tags_processed
        return redirect(url_for('index'))
