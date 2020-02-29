# def account(name, number, balance):
#     return {'name': name, 'number': number, 'balance': balance}

# def deposit(acct, amount):
#     if amount <= 0:
#          raise ValueError('amount must be positive')
#     acct['balance'] += amount 

# def withdraw(acct, amount):
#     if amount > acct['balance']:
#         raise RuntimeError('balance not enough')
#     acct['balance'] -= amount

# def to_str(acct):
#     return 'Account:' + str(acct)
class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError()('balance not enough')
        self.balance -= amount

    def __str__(self):
        return 'Account({0}, {1}, {2})'.format(
            self.name, self.number, self.balance
        )