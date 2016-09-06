#!venv/bin/python
# -*- coding:utf8 -*-
from flask import Flask
app = Flask('__main__')

@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run()
