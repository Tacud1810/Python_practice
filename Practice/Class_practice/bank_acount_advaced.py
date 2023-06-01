# Create a class called BankAccount that represents a bank account for a user. The class should have attributes
# such as account_number (account number), owner (account owner), and balance (account balance). Include methods to
# deposit and withdraw funds from the account, calculate interest based on a specified interest rate, and check
# the account balance. Additionally, implement a method to transfer funds from one bank account to another.
# Create instances of the BankAccount class with specific values and test the methods.
# Feel free to assign specific values to the attributes and test the methods according to your requirements.

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner}\nBank account number: {self.account_number}\nBalance: {self.balance}\n"

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insuficient funds!")
        else:
            print(f"withdrawing... ")
            self.balance -= amount

    def deposit(self, amount):
        print(f"depositing... ")
        self.balance += amount

    def check_balance(self):
        print(f"Account balance: {self.balance}")

    def transfer_funds(self, destination_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            destination_account.balance += amount
        else:
            print("Insuficient funds for transfer")

    def calculate_interest(self, amount, rate):
        return (amount * (rate / 100)) + amount


radek = BankAccount(125478, "Radek Rich", 520)
richard = BankAccount(254698, "Richard Poor", 250)

print(radek)
radek.deposit(520)
radek.check_balance()
print(radek)
radek.withdraw(250)
print(radek)
radek.withdraw(10)

radek.transfer_funds(richard, 250)
print(radek)
print(richard)
print(radek.calculate_interest(20000, 6.5))
