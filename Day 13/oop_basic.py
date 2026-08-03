class Student: #self is a reference to the current instance of the class.
    def greet(self):
        print("Hello, I am a student.")

student1 = Student()
student1.greet()

#__init__ is a special method in Python classes, also known as a constructor. It is automatically called when a new instance of the class is created. The purpose of the __init__ method is to initialize the attributes of the class.

class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student2 = Student("Parth", 20, "AIML")
print(student2.name)
print(student2.age)
print(student2.course)

#creating multiple objects
class Data:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

data1 = Data("Parth", 20, "Aiml")
data2 = Data("Amaya", 20, "Aiml")
data3 = Data("Prathmesh", 20, "Aiml")

print(data1.name)
print(data2.name)
print(data3.name)

#Method: it is a funtion defined inside a class.
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Hello, my name is",self.name,"and I am ",self.age,"years old. I am studying", self.course)

student3 = Student("Parth", 20, "AIML")
student3.introduce()
