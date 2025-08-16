from pymongo import MongoClient

# Connect to MongoDB running locally (for now, develop step)
client = MongoClient("mongodb://localhost:27017/")

# Use database "budget_manager"
db = client["budget_manager"]

# Use collection "expenses"
expenses_collection = db["expenses"]


# Save an expense
def save_expense(expense):
    expenses_collection.insert_one(expense)


# Load all expenses
def load_expenses():
    return list(expenses_collection.find({}, {"_id": 0}))  # exclude _id field for cleaner output
