#Public Attributes
class Student:
    def __init__(self,name):
        self.name = name

student = Student("Parth")
print(student.name) #Parth

#private attributes
class BankAcc:
    def __init__(self,balance):
        self.__balance = balance

#account = BankAcc(5000)
#print(account.__balance) #AttributeError: 'BankAcc' object has no attribute '__balance'

#Accessing private attributes.
class BankAcc:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        print("Balance:",self.__balance)

account = BankAcc(5000)
account.get_balance() #Balance: 5000

#deposit and withdraw methods
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

account = BankAccount(5000)
account.deposit(2000)
account.show_balance()

class BankAcc:
    def __init__(self,balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful. New balance:", self.__balance)

    def show_balance(self):
        print("Current balance:", self.__balance)

account = BankAcc(5000)
account.withdraw(2000)  # Withdrawal successful. New balance: 3000
account.show_balance()   # Current balance: 3000