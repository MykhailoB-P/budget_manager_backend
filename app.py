from flask import Flask, request, jsonify
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

# 
# Function for saving expenses as a data
def save_expenses(expenses):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)

# Welcoming route
@app.route('/')
def hello_world():
    return 'Hello world, my budget manager is here!'

# Expenses route
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()  # get JSON data from the request
    if not data or 'amount' not in data or 'category' not in data:
        return jsonify({"error": "Fields 'amount' and 'category' are required"}), 400

 # Amount validation
    try:
        amount = float(data['amount'])
    except ValueError:
        return jsonify({"error": "Amount must be a number"}), 400

    # Category validation
    category = str(data['category']).strip()
    if not category:
        return jsonify({"error": "Category cannot be empty"}), 400


    expense = {
        "amount": float(data['amount']),
        "category": data['category'],
        "date": data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    return jsonify(expense), 201

# Route to get all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = load_expenses()
    return jsonify(expenses)

# Route to get statistics by category
@app.route('/stats', methods=['GET'])
def get_stats():
    expenses = load_expenses()
    stats = {}
    for exp in expenses:
        category = exp['category']
        stats[category] = stats.get(category, 0) + exp['amount']
    return jsonify(stats)


if __name__ == '__main__':
    app.run(debug=True)
