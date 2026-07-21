#Creating tuples
fruits = ("apple","banana","orange")
print(fruits)

#Accessing elements
fruits = ("apple","banana","orange")
print(fruits[0])
print(fruits[2])

#negative indexing
print(fruits[-1])

#slicing
numbers = (10,20,30,40,50)
print(numbers[1:4])

#tuple length
print(len(numbers))

#count method
number = (1,2,2,3,4,5)
print(number.count(2))

#index method
number = (1, 10, 15, 20)
print(number.index(15))

#loop through tuple
fruits = ("apple","banana","orange")
for fruit in fruits:
    print(fruit)

#Packing means storing multiple values in one tuple
student = ("Parth",20,"AIML")

#Unpacking
name, age, department = student
print(name)
print(age)
print(department)

#Tuple inside tuple
student = (
    ("Parth", 20, "AIML"),
    ("Prathmesh", 20, "AIML"),
    ("Amay", 21, "AIML")
)
print(student[1])

print(student[2][1])