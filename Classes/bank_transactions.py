
# Dave, Sara, DaveIAA, Jim, Nancy are all objects

from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()

Sara.getBalance()

Dave.deposit(250)
Sara.deposit(500)


Dave.withdraw(300)

Dave.transfer(400, Sara)


DaveIAA = InterestAwardsAcct(100, 'DaveIAA')

#this deposit will attract 5% interest (note balance after this is $625 and not $600)
# the additional $25 is $500 * 5% interest rate
DaveIAA.deposit(500)

Jim = InterestAwardsAcct(1000, 'Jim')

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(250, Dave)

# this transfer will hit an error condition as transfer value exceeds account balance
Jim.transfer(5000, DaveIAA)

# this transfer will process successfully
Jim.transfer(500, DaveIAA)

Nancy = SavingsAcct(1000, "Nancy")

Nancy.withdraw(200)

