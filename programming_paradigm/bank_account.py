# Class Definition:

# Define a class named BankAccount.
# Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
# Encapsulation and Behaviors:

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.


class BankAccount:
    def __init__ (self, account_balance = 0) :
        self.account_balance = account_balance

    def deposit(self,amount):
        return amount + self.account_balance
    
    def withdraw(self,amount):
        if self.account_balance - amount >= 0 :
            return True and self.account_balance - amount 
        else :
            return False 

    def display_balance(self):
           
        print(f'Current Balance: ${self.account_balance:.2f}')   