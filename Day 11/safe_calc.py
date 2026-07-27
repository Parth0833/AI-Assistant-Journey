#Safe Calculator
def safe_calculator():
    while True:
        # Display the menu options
        print("\n--- Safe Calculator ---")
        print("1 Addition")
        print("2 Subtraction")
        print("3 Multiplication")
        print("4 Division")
        print("5 Exit")

        # Get menu choice from user
        choice = input("Choose an option (1-5): ").strip()

        # Exit condition
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        # Check for invalid menu selection
        if choice not in ["1", "2", "3", "4"]:
            print("Error: Invalid option! Please choose a number between 1 and 5.")
            continue

        # Safely prompt for the two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input! Please enter valid numeric values.")
            continue

        # Perform calculation based on choice
        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            try:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")


# Run the program
safe_calculator()
