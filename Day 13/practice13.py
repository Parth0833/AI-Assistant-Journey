#Create a Person class containing name and age. Create two objects and print their information.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)

person1 = Person("Parth", 20)
person2 = Person("Amay", 21)
person1.info()
print()
person2.info()

print("="*20)

#Create a Rectangle class containing length and width. Add an area() method that prints the area.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        area1 = self.length * self.width
        print("Area of rectangle is:",area1)

rect1 = Rectangle(5,11)
rect1.area()
print("="*20)
#Create a Student class containing name and marks. Add a method that prints "Pass" when marks are
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

student1 = Student("Parth", 100)
student2 = Student("Amay", 35)
student1.result()
student2.result()
