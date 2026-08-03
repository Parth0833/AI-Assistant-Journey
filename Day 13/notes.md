# Day 13 – Object-Oriented Programming Part 1

## Topics Learned

- Object-Oriented Programming
- Classes
- Objects
- Attributes
- Methods
- self
- __init__()

## Important Concepts

Class = Blueprint

Object = Instance of a class

Attribute = Information/data belonging to an object

Method = Function belonging to a class

self = Refers to the current object

__init__() = Initializes an object's attributes when the object is created

## Example

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

student1 = Student("Parth", 20)

student1.display()