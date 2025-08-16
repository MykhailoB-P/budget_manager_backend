from flask import Blueprint, request, jsonify
from utils import load_expenses, save_expense
from datetime import datetime

# Create Blueprint
api = Blueprint('api', __name__)

# Home route
@api.route('/')
def home():
    return 'Hello world, my budget manager is here!'

# POST route to add expense
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

    saved_expense = save_expense(expense)  # now includes _id as string
    return saved_expense, 201

# GET route to get all expenses
@api.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(load_expenses())
