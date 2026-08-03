# Parent Class
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        """Common method for all Person objects"""
        return f"Hi, I am {self.name} and I am {self.age} years old."


# Child Class 1
class Teacher(Person):

    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        """Teacher-specific method"""
        return f"{self.name} is teaching {self.subject}."


# Child Class 2
class Student(Person):

    def __init__(self, name: str, age: int, marks: float):
        super().__init__(name, age)
        self.marks = marks

    def study(self):
        """Student-specific method"""
        return f"{self.name} is studying hard to improve their score of {self.marks}."


# Example Usage
if __name__ == "__main__":
    # Create instances
    teacher = Teacher(name="Mr. Davis", age=40, subject="Mathematics")
    student = Student(name="Emma", age=16, marks=92.5)

    # Common method call
    print("--- Introductions ---")
    print(teacher.introduce())
    print(student.introduce())

    # Specific method calls
    print("\n--- Specific Actions ---")
    print(teacher.teach())
    print(student.study())