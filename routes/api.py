from utils import load_expenses, save_expense

# POST route
@api.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or 'amount' not in data or 'category' not in data:
        return {"error": "Fields 'amount' and 'category' are required"}, 400

    expense = {
        "amount": float(data['amount']),
        "category": data['category'],
        "date": data.get('date')
    }

    save_expense(expense)
    return expense, 201

# GET route
@api.route('/expenses', methods=['GET'])
def get_expenses():
    return load_expenses()
