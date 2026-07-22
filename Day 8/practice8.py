#Create a student Dictionary
student ={
    "name":"Parth",
    "age": 20,
    "course":"AIML"
}
print(student)

student["city"]="Kalyan"
print(student)

student["age"] = 21
print(student)

student.pop("age")
print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ":", value)

#create a dictionary of 5 subject and marks
marks = {
    "sub1": {"name": "maths", "mark": 90},
    "sub2": {"name": "English", "mark": 80},
    "sub3": {"name": "History", "mark": 85},
    "sub4": {"name": "Geography", "mark": 95},
    "sub5": {"name": "Marathi", "mark": 100},
}

all_marks = [sub["mark"] for sub in marks.values()]

max_mark = max(all_marks)
min_mark = min(all_marks)
avg = sum(all_marks) / len(all_marks)

highest_subject = max(marks.values(), key=lambda x: x["mark"])
lowest_subject = min(marks.values(), key=lambda x: x["mark"])

# Output results
print("Highest mark:", max_mark, f"({highest_subject['name']})")
print("Lowest mark:", min_mark, f"({lowest_subject['name']})")
print("Average of all subject marks is:", avg)

#get 
print(student.get("phone","Not Available"))