class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

adrien = User("Adrien", "")
nibbles = User("Mr. Nibbles", "")
benny = User("Benny Bob", "")

adrien.make_deposit(500).make_deposit(250).make_deposit(750).make_withdrawal(200).display_user_balance()

nibbles.make_deposit(200).make_deposit(1000).make_withdrawal(300).make_withdrawal(800).display_user_balance()

benny.make_deposit(2000).make_withdrawal(500).make_withdrawal(1200).make_withdrawal(300).display_user_balance()

adrien.transfer_money(benny, 300).display_user_balance()
benny.display_user_balance()