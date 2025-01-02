class BalanceException(Exception):
    pass



class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"""\nAccount '{self.name}' created. 
            \nBalance = ${self.balance:.2f}\n""")
        

    def getBalance(self):
        print(f"\nAccount {self.name} balance = ${self.balance:.2f}\n")

    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit transaction completed")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}')

    #14.45 mins
    def transfer(self, amount, target_account):
        try: 
            print("\n***********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            target_account.deposit(amount)
            print('\n Transfer Complete! ✅\n\n***********')
        except BalanceException as error:
            print(f'\nTransfer interrupted: ❌ {error}')
            print("\nTransfer failed. Please try again.\n")

class InterestAwardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit Complete.')
        self.getBalance()


class SavingsAcct(InterestAwardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\n${amount} withdraw complete. Fee of ${self.fee}")
            self.getBalance()        
        except BalanceException as error:
            print(f'\nWithdrawal from Savings Account interrupted: {error}')




    



    
