def atm_simulator():
    balance = 0.0  # Starting balance

    while True:
        # Display Menu
        print("\n=== ATM Simulator ===")
        print("1 Check Balance")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Exit")

        # Get menu option
        choice = input("Select an option (1-4): ").strip()

        # Handle Exit
        if choice == "4":
            print("\nThank you for using our ATM. Goodbye!")
            break

        # Handle Invalid Menu Choice
        if choice not in ["1", "2", "3"]:
            print("Error: Invalid option. Please select a number between 1 and 4.")
            continue

        # Option 1: Check Balance
        if choice == "1":
            print(f"\nYour current balance is: ${balance:.2f}")

        # Option 2: Deposit
        elif choice == "2":
            try:
                amount = float(input("\nEnter amount to deposit: $"))
                if amount <= 0:
                    print("Error: Deposit amount must be greater than zero.")
                else:
                    balance += amount
                    print(f"Success! Deposited ${amount:.2f}.")
                    print(f"New Balance: ${balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid numerical amount.")

        # Option 3: Withdraw
        elif choice == "3":
            try:
                amount = float(input("\nEnter amount to withdraw: $"))
                if amount <= 0:
                    print("Error: Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print(f"Error: Insufficient funds. Your balance is ${balance:.2f}.")
                else:
                    balance -= amount
                    print(f"Success! Withdrew ${amount:.2f}.")
                    print(f"New Balance: ${balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid numerical amount.")


# Run the ATM Simulator
atm_simulator()