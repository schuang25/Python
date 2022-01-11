class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount()]

    # Account number passed in as is normally done, and modified in-method to properly handle list indices
    def make_deposit(self, amount, account_no):	
        self.accounts[account_no-1].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_no):
        self.accounts[account_no-1].withdraw(amount)
        return self

    def transfer_money(self, my_acc, other_user, other_acc, amount):
        if (self.accounts[my_acc-1].balance > amount): # Can only transfer money if there is enough in the balance
            self.accounts[my_acc-1].withdraw(amount)
            other_user.accounts[other_acc-1].deposit(amount)
        else: # Still need to charge fee
            self.accounts[my_acc-1].withdraw(amount)
        return self

    def display_account_balance(self, account_no):
        print(f"User: {self.name}, Account Number: {str(account_no)} Balance: {self.accounts[account_no-1].balance}")
        return self

    def display_all_accounts(self):
        print(f"User: {self.name}")
        for x in range(0, len(self.accounts)):
            print(f"Account Number: {str(x+1)}, Balance: {self.accounts[x].balance}")
        return self

    def add_account(self, int_rate=0.01, balance=0):
        self.accounts.append(BankAccount(int_rate, balance))
        print (f"{self.name} now has {str(len(self.accounts))} accounts")
        return self

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

adrien = User("Adrien", "")
adrien.make_deposit(500, 1).make_deposit(200, 1).make_withdrawal(300, 1).display_account_balance(1)
adrien.add_account()
adrien.make_deposit(500, 1).transfer_money(1, adrien, 2, 300).display_all_accounts()