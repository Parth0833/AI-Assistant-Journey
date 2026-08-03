class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee name:", self.name)
        print("Employee Salary:", self.salary)

    def salary_raise(self, amount):
        self.amount = amount
        self.salary += self.amount
        print("Salary Increased by:",self.amount)
        print("New Salary:",self.salary)

employee1 = Employee("Parth", 50000)
employee1.display_info()
employee1.salary_raise(10000)
employee1.display_info()
