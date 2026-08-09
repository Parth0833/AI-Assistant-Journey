import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file if it exists."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_contacts(contacts):
    """Saves the list of contacts to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Adds a new contact to the list."""
    print("\n--- Add Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact for '{name}' added successfully!")

def search_contact(contacts):
    """Searches for contacts by name."""
    print("\n--- Search Contact ---")
    search_name = input("Enter name to search: ").strip().lower()
    
    results = [c for c in contacts if search_name in c["Name"].lower()]

    if results:
        print(f"\nFound {len(results)} matching contact(s):")
        for contact in results:
            print(f"Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")
    else:
        print(f"No contacts found matching '{search_name}'.")

def update_contact(contacts):
    """Updates an existing contact's details."""
    print("\n--- Update Contact ---")
    search_name = input("Enter the name of the contact to update: ").strip().lower()
    
    for contact in contacts:
        if contact["Name"].lower() == search_name:
            print(f"Updating '{contact['Name']}' (leave blank to keep current value):")
            
            new_name = input(f"New Name [{contact['Name']}]: ").strip()
            new_phone = input(f"New Phone [{contact['Phone']}]: ").strip()
            new_email = input(f"New Email [{contact['Email']}]: ").strip()

            if new_name:
                contact["Name"] = new_name
            if new_phone:
                contact["Phone"] = new_phone
            if new_email:
                contact["Email"] = new_email

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print(f"No contact found with the name '{search_name}'.")

def delete_contact(contacts):
    """Deletes a contact by name."""
    print("\n--- Delete Contact ---")
    delete_name = input("Enter the name of the contact to delete: ").strip().lower()
    
    initial_count = len(contacts)
    updated_contacts = [c for c in contacts if c["Name"].lower() != delete_name]

    if len(updated_contacts) < initial_count:
        contacts.clear()
        contacts.extend(updated_contacts)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print(f"No contact found with the name '{delete_name}'.")

def show_all_contacts(contacts):
    """Displays all saved contacts."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")

def main():
    contacts = load_contacts()

    while True:
        print("\n==============================")
        print("📖 Contact Book System")
        print("==============================")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            show_all_contacts(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

