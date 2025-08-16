from database import expenses_collection
from datetime import datetime
from bson.objectid import ObjectId

def load_expenses():
    expenses = list(expenses_collection.find())
    # Convert ObjectId to string for JSON serialization
    for e in expenses:
        e["id"] = str(e["_id"])
    return expenses

def save_expense(expense):
    if "date" not in expense:
        expense["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Insert into MongoDB
    result = expenses_collection.insert_one(expense)
    expense["_id"] = str(result.inserted_id)  # convert ObjectId to string
    return expense
