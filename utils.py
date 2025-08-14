import json
import os

DATA_FILE = 'expenses.json'

# Function for adding expenses
def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Function for saving expenses as a data
def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)
