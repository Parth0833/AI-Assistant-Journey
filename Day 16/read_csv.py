import csv
with open("Day 16/student.csv","r") as files:
    reader = csv.reader(files)
    for row in reader:
        print(row)
print("="*30)
#for skipping the header
#import csv
#with open("Day 16/student.csv","r") as file:
#    reader = csv.reader(file)
#    next(reader)
#    for row in reader:
#        print(row)
#    print("="*30)

#writing to csv
import csv 
with open("Day 16/student.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Course"])
    writer.writerow(["Parth", 20, "AIML"])
    writer.writerow(["Amaya", 20, "AIML"])
    writer.writerow(["Prathmesh", 21, "AIML"])
#for multiple writing.
import csv

students = [
    ["Parth", 20, "AIML"],
    ["Rahul", 21, "CSE"],
    ["Amit", 19, "IT"]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])

    writer.writerows(students)

#Dictreader
import csv
with open("Day 16/student.csv","r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(student)
    
print("="*50)

import csv
with open("Day 16/student.csv","r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(student["Name"], "-", student["Course"])

#Dictwriter
import csv
students = [
    {
        "Name":"Parth",
        "Age":20,
        "Course":"AIML"
    },
    {
        "Name":"Amaya",
        "Age":20,
        "Course":"AIML"
    }
]
with open("Day 16/student.csv","w",newline="") as file:
    fieldnames = ["Name","Age","Course"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
