from database import expenses_collection
from datetime import datetime

def load_expenses():
    # Return all expenses as a list
    return list(expenses_collection.find({}, {"_id": 0}))

def save_expense(expense):
    # Add date if not exists
    if "date" not in expense:
        expense["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Insert into MongoDB
    expenses_collection.insert_one(expense)
