class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance 


account = BankAccount("9487027110")
account.deposit(5000)
account.withdraw(2500)
print("Current balance:", account.get_balance())