class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance.")

    def show_balance(self):
        print("Your current balance is:", self.balance)

account1 = Bank("Parth", 1000)
account1.show_balance()
print()
account1.deposit(1000)
print()
print("After depositing 1000:")
account1.show_balance()
account1.withdraw(100)
print()
print("After withdrawing 100:")
account1.show_balance()