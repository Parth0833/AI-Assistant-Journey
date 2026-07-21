#Create tuple of 5 fruits print each fruit
fruits = ("Apple","Mango","Orange","Banana","Watermelon")
for fruit in fruits:
    print(fruit)

#Create a tuple of number print largest smallest and sum 
numbers = (20, 30, 80, 50)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Count how many times a number appear
number = (1,2,2,4,4,5,5,5,5,6,6,6,6,1,1,7,1,1)
print(number.count(1))

#Find index of an element
print(numbers.index(80))

#Use tuple unpacking
student = ("Parth",20,"AIML")

name, age, department = student
print(name)
print(age)
print(department)

#Create a nested tuple for student name and marks
student = (
    ("Parth",90),
    ("Prathmesh",89),
    ("Amay",98)
)
print(student[2])
print(student[0][1])
