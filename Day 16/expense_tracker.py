import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    """Loads expense records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """Saves the expenses list to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Adds a new expense category and amount."""
    print("\n--- Add Expense ---")
    category = input("Enter category (e.g., Food, Travel): ").strip()
    
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")

    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense of {amount} under '{category}' added successfully!")

def view_expenses(expenses):
    """Displays all recorded expenses and total spent."""
    print("\n--- View Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. Category: {item['category']} | Amount: {item['amount']}")
        total += item['amount']

    print("-" * 35)
    print(f"Total Expenses: {total}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n==============================")
        print("💸 Expense Tracker")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()