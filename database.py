from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create/use database
db = client["budget_manager"]

# Create/use collection
expenses_collection = db["expenses"]
