class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            x = float(amount)
            if x > 0:
                self.balance += x
                print('Deposit accepted')
            else:
                print('Invalid amount')
        except:
            print('Invalid amount')

    def withdraw(self, amount):
        try:
            x = float(amount)
            if x > 0 and x <= self.balance:
                self.balance -= x
                print('Withdrawal accepted')
            elif x == 0:
                print('Invalid amount')
            else:
                print('Funds Unavailable!')
        except:
            print('Invalid amount')

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'


acct1 = Account('Jose',100)
print(acct1)
acct1.deposit(10)
acct1.withdraw(0)
print(acct1.balance)
