#Ascending order
students=[
    ("Parth",19),
    ("Amay",21),
    ("Prathmesh",20)
]
students.sort(key=lambda student:student[1])
print("In Ascending Order:",students)

#Descending order
students=[
    ("Parth",19),
    ("Amay",21),
    ("Prathmesh",20)
]
students.sort(key=lambda student:student[1], reverse=True)
print("In Descending order:",students)

