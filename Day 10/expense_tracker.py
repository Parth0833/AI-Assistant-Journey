def add_expense():
    category = input("Enter expense category (e.g., Food, Travel, Books): ").strip()
    amount = input("Enter amount spent: ").strip()

    # Format the string to match: Category - $Amount
    entry = f"{category} - ${amount}"

    # Append entry to expenses.txt
    with open("expenses.txt", "a") as file:
        file.write(entry + "\n")

    print(f"Added expense: '{entry}' successfully!\n")


def view_expenses():
    print("\n--- Saved Expenses ---")
    try:
        with open("expenses.txt", "r") as file:
            content = file.read()
            if content.strip():
                print(content, end="")
            else:
                print("No expenses logged yet.")
    except FileNotFoundError:
        print("No expenses found. Add an expense first!")
    print("---------------------\n")


def main():
    while True:
        print("Expense Tracker")
        print("Menu:")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()