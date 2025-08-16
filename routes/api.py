from flask import Blueprint, request, jsonify
from datetime import datetime
from utils import validate_expense, format_date
from database import add_expense, get_all_expenses, get_expense_stats

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'Hello world, my budget manager is here!'

@api.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    errors = validate_expense(data)
    if errors:
        return jsonify({"errors": errors}), 400

    expense = {
        "amount": data["amount"],
        "category": data["category"],
        "date": format_date(data.get("date", datetime.now()))
    }

    add_expense(expense)
    return jsonify(expense), 201

@api.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(get_all_expenses())

@api.route('/stats', methods=['GET'])
def get_stats():
    return jsonify(get_expense_stats())
