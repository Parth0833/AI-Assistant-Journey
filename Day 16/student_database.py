import json
import os

FILE_NAME = "students.json"

def load_students():
    """Loads student records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_students(students):
    """Saves the student records list to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    """Adds a new student to the database."""
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    course = input("Enter student course: ").strip()

    student = {
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(student)
    save_students(students)
    print(f"Student '{name}' added successfully!")

def view_students(students):
    """Displays all student records."""
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return

    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")

def search_student(students):
    """Searches for a student by name."""
    print("\n--- Search Student ---")
    search_name = input("Enter name to search: ").strip().lower()
    
    found_students = [
        s for s in students if search_name in s['name'].lower()
    ]
    
    if found_students:
        print("\nMatching Record(s) Found:")
        for student in found_students:
            print(f"Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")
    else:
        print(f"No student found with name matching '{search_name}'.")

def delete_student(students):
    """Deletes a student by name."""
    print("\n--- Delete Student ---")
    delete_name = input("Enter name of student to delete: ").strip().lower()
    
    initial_length = len(students)
    updated_students = [
        s for s in students if s['name'].lower() != delete_name
    ]
    
    if len(updated_students) < initial_length:
        save_students(updated_students)
        students.clear()
        students.extend(updated_students)
        print(f"Student record deleted successfully.")
    else:
        print(f"No student found with name '{delete_name}'.")

def main():
    students = load_students()
    
    while True:
        print("\n==============================")
        print("🚀 Student Database System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting Student Database System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()