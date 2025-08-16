from pymongo import MongoClient

# Connect to MongoDB running locally (for now, develop step)
client = MongoClient("mongodb://localhost:27017/")

# Use database "budget_manager"
db = client["budget_manager"]

# Use collection "expenses"
expenses_collection = db["expenses"]
    
# Load all expenses
def load_expenses():
    return list(expenses_collection.find({}, {"_id": 0}))  # exclude _id field for cleaner output

# Save an expense
def save_expense(expense):
    if "date" not in expense:
        expense["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses_collection.insert_one(expense)