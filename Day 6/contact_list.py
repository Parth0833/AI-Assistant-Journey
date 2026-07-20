contact_list = {}

while True:
    print("\n--- Menu ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Display Contacts")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        number = input("Enter phone number: ").strip()

        if name and number:
            contact_list[name] = number
            print(f"Contact '{name}' added successfully.")
        else:
            print("Error: Name and number cannot be empty.")

    elif choice == "2":
        if not contact_list:
            print("Contact list is empty.")
        else:
            name = input("Enter the name to remove: ").strip()
            if name in contact_list:
                del contact_list[name]
                print(f"Contact '{name}' removed successfully.")
            else:
                print(f"Contact '{name}' not found.")

    elif choice == "3":
        if not contact_list:
            print("Contact list is empty.")
        else:
            print("\nSaved Contacts:")
            for name, number in contact_list.items():
                print(f"• {name}: {number}")

    elif choice == "4":
        if not contact_list:
            print("Contact list is empty.")
        else:
            name = input("Enter the name to search: ").strip()
            if name in contact_list:
                print(f"Found: {name} -> {contact_list[name]}")
            else:
                print(f"No contact found for '{name}'.")

    elif choice == "5":
        print("Thanks for visiting!")
        break

    else:
        print("Invalid input! Please select a number between 1 and 5.")