# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f"✓ '{task}' added successfully.")
    else:
        print("Task cannot be empty!")

def remove_task():
    if not tasks:
        print("Your list is empty. Nothing to remove!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"✓ Removed '{removed}'.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is currently empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        # Using if-elif-else logic
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye! Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()