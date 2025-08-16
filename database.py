from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # default local MongoDB
db = client["budget_manager"]                        # database name
expenses_collection = db["expenses"]                 # collection name

# Add a new expense
def add_expense_db(expense):
    if "date" not in expense:
        expense["date"] = datetime.now()
    return expenses_collection.insert_one(expense)

# Get all expenses
def get_all_expenses():
    return list(expenses_collection.find({}, {"_id": 0}))  # hide _id for cleaner JSON

# Get stats by category
def get_stats():
    stats = {}
    for exp in get_all_expenses():
        category = exp["category"]
        stats[category] = stats.get(category, 0) + exp["amount"]
    return stats