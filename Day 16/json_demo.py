import json
student ={
    "name":"Parth",
    "age": 20,
    "course":"AIML"
}
with open("Day 16/student.json","w") as file:
    json.dump(student,file,indent=4)

#reading json 
import json
with open("Day 16/student.json","r") as file:
    student = json.load(file)
print(student)
