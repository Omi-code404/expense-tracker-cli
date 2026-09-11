import json
import os
file_name="expenses.json"

def load_expenses():
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(file_name,"w") as f:
        json.dump(expenses,f,indent=4)

def view_all(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for i,e in enumerate(expenses,start=1):
         print(f"{i}. {e['category']} - {e['amount']}  {e['note']}")
def add_expense(expenses):
    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        note = input("Enter a note (optional): ")
        expense = {"amount": amont, "category": category, "note": note}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
print("For example")
sample = [{"amount": 200, "category": "Food", "note": "Lunch"}]
view_all(sample)      