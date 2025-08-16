from datetime import datetime

def format_date(date_obj):
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

def validate_expense(data):
    errors = []
    if "amount" not in data:
        errors.append("Field 'amount' is required")
    else:
        try:
            data["amount"] = float(data["amount"])
        except ValueError:
            errors.append("Amount must be a number")
    if "category" not in data or not data["category"].strip():
        errors.append("Field 'category' is required and cannot be empty")
    return errors

DEFAULT_CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Other"]
