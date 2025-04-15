class Account:
    """Base class representing a generic bank account."""
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f} into account {self.account_number}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account #{self.account_number} Holder: {self.holder_name} Balance: ${self.balance:.2f}"


class SavingsAccount(Account):
    """Savings account with an interest rate."""
    def __init__(self, account_number, holder_name, interest_rate, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ${interest:.2f} added to Savings Account {self.account_number}.")

    def __str__(self):
        return (f"Savings Account #{self.account_number} Holder: {self.holder_name} "
                f"Balance: ${self.balance:.2f} Interest Rate: {self.interest_rate:.1f}%")


class CheckingAccount(Account):
    """Checking account with an overdraft limit."""
    def __init__(self, account_number, holder_name, overdraft_limit, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from Checking Account {self.account_number}.")
        else:
            print("Withdrawal exceeds overdraft limit.")

    def __str__(self):
        return (f"Checking Account #{self.account_number} Holder: {self.holder_name} "
                f"Balance: ${self.balance:.2f} Overdraft Limit: ${self.overdraft_limit:.2f}")


def main():
    # Create a savings account
    savings = SavingsAccount("SA001", "John Smith", interest_rate=5.0, initial_balance=1000.0)
    savings.deposit(100)
    savings.add_interest()
    savings.withdraw(50)

    # Create a checking account
    checking = CheckingAccount("CA001", "Jane Doe", overdraft_limit=100.0, initial_balance=0.0)
    checking.withdraw(50)  # This should be allowed
    checking.withdraw(100) # This should not be allowed

    # Print account details
    print()
    print(savings)
    print(checking)


# Run the program
if __name__ == "__main__":
    main()
