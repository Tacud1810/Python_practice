# Create a class called BankAccount that represents a bank account for a user. The class should have attributes
# such as account_number (account number), owner (account owner), and balance (account balance). Add a method
# called deposit() that takes an amount as input and adds it to the balance attribute. Also, add a method
# called withdraw() that takes an amount as input and subtracts it from the balance if sufficient funds are
# available. Create an instance of the BankAccount class with specific values and test the deposit() and
# withdraw() methods.


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


radek = BankAccount(125478, "Radek Rich", 520)

print(radek)
radek.deposit(520)
print(radek)
radek.withdraw(250)
print(radek)
radek.withdraw(810)
