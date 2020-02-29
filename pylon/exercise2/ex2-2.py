import package._bank as bank
# acct = bank.account('Justin', '123-4567', 1000)
acct = bank.Account('Justin', '123-3567', 1000)
acct.deposit(500)
acct.withdraw(200)
# print(acct.to_str(acct))
print(acct)