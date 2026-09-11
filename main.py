import json
import os
File_Name="expenses.json"

def load_expenses():
    if not os.path.exists(File_Name):
        return []
    with open(File_Name, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(File_Name,"w") as f:
        json.dump(expenses, f, indent=4)

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
        expense = {"amount": amount, "category": category, "note": note}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

print("For example")
sample = [{"amount": 200, "category": "Food", "note": "Lunch"}]
view_all(sample)
def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View All\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice")
if __name__ == "__main__":
    main()
