# Phone Book Storage: Name -> Phone Number
phone_book = {}


def show_menu():
    print("\n" + "=" * 25)
    print("      PHONE BOOK")
    print("=" * 25)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show Contacts")
    print("5. Exit")
    print("=" * 25)


def phone_book_app():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        # 1. Add Contact
        if choice == "1":
            name = input("Enter contact name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue

            phone = input("Enter phone number: ").strip()
            phone_book[name] = phone
            print(f"✅ Contact '{name}' saved successfully!")

        # 2. Search Contact
        elif choice == "2":
            name = input("Enter contact name to search: ").strip()
            if name in phone_book:
                print(f"🔍 Found: {name} -> {phone_book[name]}")
            else:
                print(f"❌ Contact '{name}' not found.")

        # 3. Delete Contact
        elif choice == "3":
            name = input("Enter contact name to delete: ").strip()
            if name in phone_book:
                del phone_book[name]
                print(f"🗑️ Contact '{name}' deleted successfully.")
            else:
                print(f"❌ Contact '{name}' not found.")

        # 4. Show Contacts
        elif choice == "4":
            if not phone_book:
                print("📭 Phone book is currently empty.")
            else:
                print("\n--- Saved Contacts ---")
                for name, phone in phone_book.items():
                    print(f"{name} -> {phone}")

        # 5. Exit
        elif choice == "5":
            print("👋 Exiting Phone Book. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")


# Run the application
if __name__ == "__main__":
    phone_book_app()