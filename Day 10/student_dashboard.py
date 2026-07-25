def add_student():
    name = input("Enter student name: ").strip()
    marks = input("Enter student marks: ").strip()

    # Append the student record to students.txt on a new line
    with open("students.txt", "a") as file:
        file.write(f"{name} {marks}\n")

    print(f"Record for '{name}' added successfully!\n")


def display_records():
    print("\n--- Student Records ---")
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if records:
                for line in records:
                    print(line.strip())
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No student records exist yet.")
    print("-----------------------\n")


def main():
    while True:
        print("Student Record System")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_records()
        elif choice == "3":
            print("Exiting Student Record System. Goodbye!")
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.\n")


# Run the application
if __name__ == "__main__":
    main()