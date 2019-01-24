#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:38:58 2019

@author: Ib Helmer Nielsen
"""
import os.path
from flask import Flask, render_template, Response
from flask_restful import Resource, Api
from gpiozero import LED

red = LED(20)

# Create the application instance
app = Flask(__name__)
api = Api(app)

# Create a URL route in our application for "/"
class home(Resource):
    def get(self):
       #content = get_file('index.html')
       return Response('<h1>Test</h1>', mimetype="text/html")
       

class ledon(Resource):
    def get(self):
       red.on()
       return Response('<h1>Led on<br></h1>', mimetype="text/html")

class ledoff(Resource):
    def get(self):
        red.off()
        return Response('<h1>Led off<br></h1>', mimetype="text/html")

api.add_resource(home,'/')
api.add_resource(ledon, '/ledon')
api.add_resource(ledoff, '/ledoff')  

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='192.168.1.100',debug=True,port=7913)