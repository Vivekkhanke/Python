""" variables:
public : self.name
protected : self._name
private : self.__name
"""
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance   #private  1000
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount    # balance += amount  1500
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount    # self.__balance -= amount
        else:
            print("Insufficient balance")
            
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)         #calling the function
acc.withdraw(2000)
print(acc.get_balance())