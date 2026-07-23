student_names = set()

print("Enter student names (type 'done' when finished):")

while True:
    name = input("Enter name: ").strip()

    # Exit the loop when the user enters 'done'
    if name.lower() == "done":
        break

    # Add the name if it's not empty
    if name:
        student_names.add(name)

# Display the set of unique student names
print("\n--- Unique Student Names ---")
print(student_names)