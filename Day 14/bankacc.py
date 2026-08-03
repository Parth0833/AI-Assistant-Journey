class BankAccount:

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        # Private attribute (prefixed with double underscore)
        self.__balance = initial_balance

    def deposit(self, amount: float) -> str:
        """Adds funds to the balance if the amount is positive."""
        if amount > 0:
            self.__balance += amount
            return f"Successfully deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount: float) -> str:
        """Deducts funds if sufficient balance exists."""
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.__balance:
            return f"Insufficient funds! Current balance is ${self.__balance:.2f}."

        self.__balance -= amount
        return f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.__balance:.2f}"

    def show_balance(self) -> str:
        """Returns current balance without exposing private variables directly."""
        return f"Account Holder: {self.account_holder} | Current Balance: ${self.__balance:.2f}"


# Example Usage
if __name__ == "__main__":
    account = BankAccount("Alice", initial_balance=500.0)

    # Check balance
    print(account.show_balance())

    # Deposit money
    print(account.deposit(200.0))

    # Withdraw money
    print(account.withdraw(150.0))

    # Attempt overdrawing
    print(account.withdraw(1000.0))