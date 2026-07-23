# Initialize an empty set to store attendance
attendance = set()

print("--- Student Attendance System ---")
print("Enter student names one by one. Type 'done' when finished.\n")

while True:
    name = input("Enter student name: ").strip()

    # Stop taking input when the user enters 'done'
    if name.lower() == "done":
        break

    # Ignore empty inputs
    if not name:
        continue

    # Prevent duplicate attendance entries with a friendly message
    if name in attendance:
        print(f"  ⚠️  '{name}' is already marked present!")
    else:
        attendance.add(name)
        print(f"  ✓ Marked present: {name}")

# Display Results
print("\n" + "=" * 30)
print(f"Total students present: {len(attendance)}")
print("Names of present students:")
for student in sorted(attendance):
    print(f" - {student}")
print("=" * 30)