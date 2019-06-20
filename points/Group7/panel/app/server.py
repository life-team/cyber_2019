# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/adminpanel")
@app.route("/adminpanel.html")
def admin():
    return render_template('adminpanel.html')


@app.route("/robots.txt")
def robot():
    with open('static/robots.txt', 'r', encoding='utf-8') as f:
        return f.read()


app.run(host='0.0.0.0', port=81, threaded=True)