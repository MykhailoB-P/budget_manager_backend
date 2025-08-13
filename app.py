from flask import Flask
import json
import os
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, my backend is working now!'

if __name__ == '__main__':
    app.run(debug=True)
