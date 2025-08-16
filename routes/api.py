from flask import Blueprint, request, jsonify
from datetime import datetime
from utils import load_expenses, save_expense

api = Blueprint('api', __name__)

# Home route
@api.route('/')
def home():
    return 'Hello world, my budget manager is here!'

# Function to add a new expense
@api.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or 'amount' not in data or 'category' not in data:
        return jsonify({"error": "Fields 'amount' and 'category' are required"}), 400

    try:
        amount = float(data['amount'])
    except ValueError:
        return jsonify({"error": "Amount must be a number"}), 400

    category = str(data['category']).strip()
    if not category:
        return jsonify({"error": "Category cannot be empty"}), 400

    expense = {
        "amount": amount,
        "category": category,
        "date": data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    return jsonify(expense), 201

# Get all expenses
@api.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = load_expenses()
    return jsonify(expenses)

# Get statistics by category
@api.route('/stats', methods=['GET'])
def get_stats():
    expenses = load_expenses()
    stats = {}
    for exp in expenses:
        category = exp['category']
        stats[category] = stats.get(category, 0) + exp['amount']
    return jsonify(stats)
