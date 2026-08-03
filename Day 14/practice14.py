#Animals
class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()

print("="*30)
#Vehicle
class Vehicle:
    def start(self):
        print("Starting the Vehicle...")

class Bike(Vehicle):
    def ride(self):
        print("Riding the Bike...")
        self.start()

bike = Bike()
bike.ride()

print("="*30)
#person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce (self):
        print("Hello, my name is", self.name, "and My age is", self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print("My student ID is", self.student_id)

student = Student("Parth", 20, "2443110175")
student.introduce()


#Bank Account
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Invalid Withdraw Amount or Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)

bank_account = BankAccount(1000)
bank_account.show_balance()
print("="*30)
bank_account.deposit(500)
bank_account.show_balance()
print("="*30)
bank_account.withdraw(200)
bank_account.show_balance()
print("="*30)

#Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee Salary:",self.__salary)


    def salary_rise(self, amount):
        self.amount = amount
        self.__salary += self.amount
        print("Salary Increased by:",self.amount)
        print("New Salary:", self.__salary)

employee = Employee("Parth", 50000)
employee.display_info()
print("="*30)
employee.salary_rise(10000)
employee.display_info()
print("="*30)