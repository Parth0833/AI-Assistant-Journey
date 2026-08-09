import csv

# File path
csv_file_path = "students.csv"

# Data: Headers and at least 5 students
students_data = [
    ["Name", "Age", "Course"],
    ["Alice", 20, "Computer Science"],
    ["Bob", 22, "Data Science"],
    ["Charlie", 21, "Mathematics"],
    ["Diana", 23, "Physics"],
    ["Ethan", 19, "Engineering"]
]

# Write data to CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("CSV file created successfully.\n")

# Read and display every student from the CSV file
print("Reading student records:")
with open(csv_file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header row
    print(f"{header[0]:<10} {header[1]:<5} {header[2]}")
    print("-" * 30)
    for row in reader:
        print(f"{row[0]:<10} {row[1]:<5} {row[2]}")

print("="*50)

import csv

csv_file_path = "Day 16/student.csv"

# Read using csv.DictReader
with open(csv_file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}")
        print(f"Course: {row['Course']}\n")

print("="*50)

import json

# Create dictionary containing name, age, course, and skills
student_data = {
    "name": "Parth",
    "age": 21,
    "course": "AIML",
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Save dictionary to student.json using json.dump()
with open("student.json", mode="w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

print("Saved student data to student.json successfully.")

print("="*50)

import json

# Read the file back using json.load()
with open("student.json", mode="r", encoding="utf-8") as file:
    student_data = json.load(file)

# Print the student's details
print(f"Name: {student_data['name']}")
print(f"Course: {student_data['course']}")
print(f"Skills: {', '.join(student_data['skills'])}")

print("="*50)

import json

# Sample data with 5 students and their marks
students = [
    {"name": "Alice", "age": 20, "course": "CS", "marks": 85},
    {"name": "Bob", "age": 22, "course": "DS", "marks": 92},
    {"name": "Charlie", "age": 21, "course": "AIML", "marks": 78},
    {"name": "Diana", "age": 23, "course": "Physics", "marks": 95},
    {"name": "Ethan", "age": 19, "course": "EE", "marks": 88}
]

# Create and save to students.json
with open("students.json", mode="w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

# Read the file back
with open("students.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

# Find the student with the highest marks
top_student = max(data, key=lambda student: student["marks"])

# Print top student details
print("Student with the highest marks:")
print(f"Name: {top_student['name']}")
print(f"Marks: {top_student['marks']}")

print("="*50)

import json

# 1. Read the JSON file
with open("students.json", mode="r", encoding="utf-8") as file:
    students_list = json.load(file)

# 2. Add a new student
new_student = {"name": "Fiona", "age": 20, "course": "Math", "marks": 91}
students_list.append(new_student)

# 3. Write the updated data back into the file
with open("students.json", mode="w", encoding="utf-8") as file:
    json.dump(students_list, file, indent=4)

print("Updated students.json with the new student.")