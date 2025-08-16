from database import expenses_collection
from datetime import datetime
from bson.objectid import ObjectId

def load_expenses():
    expenses = list(expenses_collection.find({}, {"_id": 0}))
    return expenses  # оставляем обычный список, jsonify будем делать в роуте

def save_expense(expense):
    if "date" not in expense:
        expense["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Insert into MongoDB
    result = expenses_collection.insert_one(expense)
    expense["_id"] = str(result.inserted_id)  # convert ObjectId to string
    return expense
