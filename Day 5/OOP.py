class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount): 
        self.balance -= amount

account1 = BankAccount('Sathavan',1000)
print(f"Starting balance: {account1.balance}")
print(account1.deposit(500))
print(f"Final balance: {account1.balance}")
