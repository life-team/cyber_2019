# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('task/1')


def read_tasks():
    with open('task.json', 'r', encoding='utf-8') as f:
        d = json.loads(f.read())
        return d


@app.route("/task/<int:task>")
def get_task(task):
    tasks = read_tasks()
    print(tasks[task-1])
    return render_template('index.html', tasks=tasks[task-1])


app.run(host='0.0.0.0', port=80, threaded=True)