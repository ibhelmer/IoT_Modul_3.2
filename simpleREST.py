#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:38:58 2019

@author: Ib Helmer Nielsen
"""
from flask import Flask

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    <ip address>:7913/

    :return: '<h1>Hello World!!!</h1>'
    """
    return '<h1>Hello World!!!</h1>'

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=7913)