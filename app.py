from flask import Flask
import json
import os
from datetime import datetime


app = Flask(__name__)

DATA_FILE = 'expenses.json'

# Function for adding expenses
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def hello_world():
    return 'Hello world, my backend is working now!'

if __name__ == '__main__':
    app.run(debug=True)
