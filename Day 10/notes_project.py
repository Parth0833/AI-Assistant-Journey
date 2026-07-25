def add_note():
    note = input("Enter your note: ")
    # Open file in append mode ('a') so existing notes aren't overwritten
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!\n")


def view_notes():
    print("\n--- Your Notes ---")
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content:
                print(content, end="")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found. Add a note first!")
    print("------------------\n")


def main():
    while True:
        print("Menu:")
        print("1 Add Note")
        print("2 View Notes")
        print("3 Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")


# Run the application
if __name__ == "__main__":
    main()