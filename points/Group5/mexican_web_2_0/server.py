# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route("/")
def hello():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('FLAG', 'CTF{I_AM_COOKIE}')
    return resp


app.run(host='0.0.0.0', port=8080, threaded=True)