class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
        self.interest=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (1 + self.interest)
        return self
    
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(500).deposit(300).deposit(700).withdraw(600).yield_interest().display_account_info()
account2.deposit(500).deposit(200).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()

BankAccount.all_balances()