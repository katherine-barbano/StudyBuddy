import os
from flask import Flask, request, render_template

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello"  
