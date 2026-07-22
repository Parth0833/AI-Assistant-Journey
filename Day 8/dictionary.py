#creating a dictionary
student = {
    "name":"Parth",
    "age" : 20,
    "course" : "AIML"
}

print(student)

#accessing values
student={
    "name":"Parth",
    "age": 20
}
print(student["name"])
print(student["age"])

#adding new key
student["city"]="Pune"
print(student)

#updating a value
student["age"] = 21
print(student)

#removing data
student.pop("age")
print(student)

#Dictnory lenght
print(len(student))

#loop through keys
student ={
    "name" : "Parth",
    "age" : 20,
    "cource":"AIML"
}
for key in student:
    print(key)

#loop through values
for value in student.values():
    print(value)

#loop through both
for key, value in student.items():
    print(key,":",value)

#nested dictnary
students = {
    "student1": {
        "name": "Parth",
        "marks": 92
    },

    "student2": {
        "name": "Amay",
        "marks": 87
    }
}

print(students["student1"]["marks"])

#get function
#print(student["phone"]) this will give error alternative is 
print(student.get("phone","Not Availabe"))

